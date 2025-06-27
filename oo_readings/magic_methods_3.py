class Candidate:

    def __init__(self, name):
        self.name = name
        self.votes = 0 

    def __iadd__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        self.votes += other
        return self

class Election:
    def __init__(self, candidates):
        self.candidates = candidates

    def results(self):
        max_votes = 0
        vote_count = 0
        winner = None

        for candidate in candidates:
            vote_count += candidate.votes
            if candidate.votes > max_votes:
                max_votes = candidate.votes
                winner = candidate.name 
        
        for candidate in candidates:
            name = candidate.name
            votes = candidate.votes
            print(f'{name}: {votes} votes')

        percent = 100 * (max_votes / vote_count)
        print()
        print(f'{winner} won: {percent}% of votes')

mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()


# Mike Jones: 3 votes
# Susan Dore: 4 votes
# Kim Waters: 1 votes

# Susan Dore won: 50.0% of votes