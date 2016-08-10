import datetime
import requests


def pt(type, *args):
    args_list = [str(arg) for arg in args]
    args_list.insert(0, type)
    print('\t'.join(args_list))


events = requests.get('https://api.meetup.com/Young-Programmers/events', params={
    'status': 'past',
    'key': 'your-key',
}).json()

questions = {}

def remnl(text): return text.replace('\n', '<br/>')

def fmttm(ms):
    time = int(ms) // 1000
    return datetime.datetime.fromtimestamp(time)

for event in events:
    time = fmttm(event['time'])
    duration = event.get('duration', '')
    if duration:
        duration = int(duration) / 360000.0
    fee = event['fee']['amount'] if 'fee' in event and 'amount' in event['fee'] else ''
    pt('e', time, duration, event['name'], fee, remnl(event['description']))

    comments = requests.get('https://api.meetup.com/Young-Programmers/events/%s/comments' % event['id'], params={
        'key': 'your-key',
    }).json()

    for comment in comments:
        member = comment['member']
        name = member['name']
        pt('c', name, remnl(comment['comment']))

    rsvps = requests.get('https://api.meetup.com/Young-Programmers/events/%s/rsvps' % event['id'], params={
        'key': 'your-key',
        'fields': 'attendance_status,answers'
    }).json()

    for rsvp in rsvps:
        response = rsvp['response']
        name = rsvp['member']['name']
        if response != 'no' and name != 'Dave Briccetti':
            pt('r', name, response, rsvp['guests'], rsvp.get('attendance_status', ''))
            answers = rsvp.get('answers', [])
            for answer in answers:
                a = remnl(answer['answer'])
                if a:
                    qid = answer['question_id']
                    questions[qid] = answer['question']
                    pt('a', qid, a)

for id, question in questions.items():
    pt('q', id, question)

members = []
for offset in range(3):  # Works for 483 members, which is < 200 * 3 pages  todo Make work for all
    mr = requests.get('https://api.meetup.com/Young-Programmers/members', params={
        'key': 'your-key',
        'fields': 'attendance_status,answers',
        'offset': offset
    })
    members += mr.json()

pt('m', 'ID', 'Name', 'City', 'Joined', 'Bio', 'Intro', 'Photo link')
for member in members:
    id   = member['id']
    name = member['name']
    city = member['city']
    joined = fmttm(member['joined'])
    bio  = remnl(member.get('bio', ''))
    intro = remnl(member['group_profile']['intro']) if 'group_profile' in member and 'intro' in member['group_profile'] else ''
    photo = member['photo']['highres_link'] if 'photo' in member and 'highres_link' in member['photo'] else ''
    pt('m', id, name, city, joined, bio, intro, photo)