"""Prepare proposed lab data; this script does not create Jira issues."""
import csv
import json
from pathlib import Path

OUT = Path(__file__).parent
EPICS = [
    ('E1', 'Account and access', 'Allow passengers and baggage agents to access the portal with appropriate permissions.'),
    ('E2', 'Lost luggage claims', 'Allow passengers to register and review lost luggage claims.'),
    ('E3', 'Baggage tracking', 'Help agents trace baggage and let passengers follow claim progress.'),
    ('E4', 'Notifications and compensation', 'Notify passengers of updates and support compensation requests.'),
]
STORIES = [
    ('S1', 'E1', 'Passenger sign in', 'passenger', 'sign in securely', 'access my own luggage claims', 'High', 5, 'Sprint 1', 'Valid credentials allow access; invalid credentials are rejected; passengers cannot read another passenger\'s claims.'),
    ('S2', 'E2', 'Register a missing bag', 'passenger', 'submit my flight, baggage tag and contact details', 'report a missing bag', 'High', 5, 'Sprint 1', 'Required fields are validated; a valid submission creates a unique claim reference; the passenger sees confirmation.'),
    ('S3', 'E2', 'View my claims', 'passenger', 'view my submitted claims and their status', 'check the progress of my reports', 'High', 3, 'Sprint 1', 'Only the signed-in passenger\'s claims are listed; each shows its reference and current status; an empty list is handled.'),
    ('S4', 'E1', 'Agent access control', 'baggage agent', 'access the agent dashboard using my assigned role', 'manage claims securely', 'High', 3, 'Sprint 1', 'An authorized agent can open the dashboard; a passenger cannot access agent actions; unauthorized requests are rejected.'),
    ('S5', 'E3', 'Search baggage scan records', 'baggage agent', 'search scan records by baggage tag', 'locate a reported missing bag', 'High', 5, 'Sprint 2', 'An existing tag returns ordered scan records; an unknown tag shows no results; each scan shows location and time.'),
    ('S6', 'E3', 'Update claim status', 'baggage agent', 'update a claim as its bag is located and returned', 'keep the passenger informed', 'High', 3, 'Sprint 2', 'Authorized agents can update status; invalid transitions are rejected; the change records the agent and timestamp.'),
    ('S7', 'E3', 'View tracking timeline', 'passenger', 'view the tracking timeline of my bag', 'see its last known location', 'Medium', 3, 'Sprint 2', 'The timeline shows available scans in time order; unavailable tracking is explained; access is restricted to the claim owner.'),
    ('S8', 'E4', 'Receive claim notifications', 'passenger', 'receive a notification when my claim status changes', 'learn about updates without repeatedly checking', 'Medium', 5, 'Sprint 2', 'A status change queues a notification for the claim owner; delivery failures are recorded for retry; duplicate handling avoids repeated messages for the same update.'),
    ('S9', 'E2', 'Add claim documents', 'passenger', 'attach supporting documents to my claim', 'provide the details needed to process it', 'Medium', 3, 'Backlog', 'The claim owner can attach a supported file; oversized or unsupported files are rejected; other passengers cannot access the attachment.'),
    ('S10', 'E4', 'Request compensation', 'passenger', 'submit a compensation request for an eligible claim', 'request reimbursement for my loss', 'Low', 5, 'Backlog', 'Eligibility is checked; a valid request receives a reference and pending status; a duplicate request for the same claim is rejected.'),
]

def main():
    stories = []
    for rank, row in enumerate(STORIES, 1):
        ref, epic, title, role, goal, benefit, priority, points, sprint, criteria = row
        stories.append(dict(reference=ref, epic_reference=epic, summary=title,
            description=f'As a {role}, I want to {goal}, so that I can {benefit}.',
            acceptance_criteria=criteria, priority=priority, story_points=points,
            proposed_sprint=sprint, rank=rank))
    data = dict(status='PROPOSED ONLY - not yet created or verified in Jira',
        student='MOKSHITREDDY NALLABALLE', srn='PES2UG24CS284',
        scenario='Airport Lost Luggage Claim & Tracking Portal',
        scenario_source='SELABS README and Lab 3 architecture justification; Lab 1 requirements were not available.',
        epics=[dict(reference=r, summary=s, description=d) for r, s, d in EPICS], stories=stories,
        sprint_plan=[dict(name='Sprint 1', duration_days=7, goal='Register and view luggage claims with passenger and agent access.', story_points=16),
            dict(name='Sprint 2', duration_days=7, goal='Trace bags, update claims and notify passengers.', story_points=16)],
        remaining_backlog_points=8)
    (OUT / 'proposed_backlog.json').write_text(json.dumps(data, indent=2)+'\n')
    with (OUT / 'proposed_stories.csv').open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(stories[0]))
        writer.writeheader()
        writer.writerows(stories)
    assert sum(s['story_points'] for s in stories) == 40
    for sprint in data['sprint_plan']:
        assert sum(s['story_points'] for s in stories if s['proposed_sprint'] == sprint['name']) == sprint['story_points']
    print('Prepared 4 proposed epics, 10 stories, and two 16-point sprint plans. No Jira changes made.')

if __name__ == '__main__':
    main()
