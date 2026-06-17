import random

class RLAgent:
    def __init__(self):
        self.actions = {
            'Database Failure': ['Restart Database', 'Switch Backup DB'],
            'API Failure': ['Restart API Server', 'Clear Cache'],
            'Application Error': ['Restart App', 'Rollback Deployment'],
            'Infrastructure Failure': ['Restart Container', 'Scale CPU'],
            'Deployment Failure': ['Rollback Deployment']
        }

    def choose_action(self, state):
        return random.choice(self.actions.get(state, ['Alert Developer']))
