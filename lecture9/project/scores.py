from colorama import Fore,init
init(autoreset=True)

class Scores:
    def __init__(self,player,filename = "scores.txt"):
        self.player = player
        self.filename = filename
        self.records = self.load_records()

    def save_record(self,status):
        if status.lower() == "win":
            record = {"name" : self.player.name,
                    "scores" : self.player.score,
                    "level" : self.player.level,
                    "status" : status}

            with open("scores.txt","a") as file:
                file.write(
                    f"Name : {record['name']}, Scores : {record['scores']}, Level : {record['level']}, Status : {record['status']} \n"
                )

            all_scores = self.load_records()
            high_score = max([s['scores'] for s in all_scores] or [0])
            if self.player.score >= high_score:
                print(f"{Fore.GREEN} 🥇 New High Score set by {self.player.name}: {self.player.score}!")

    def load_records(self):
        scores = []
        try:
            with open("scores.txt","r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    entry = {}
                    for p in parts:
                        k, v = p.split(":")
                        k = k.strip().lower()
                        v = v.strip()
                        if k in ["level","scores"]:
                            v = int(v)
                        entry[k] = v
                    scores.append(entry)
        except Exception as e:
            print(e)
            return scores
        return scores

    def display_records(self):
        print("\n" + "#"*40)
        print(f"{Fore.GREEN} 🏆 HALL OF FAME - HIGH SCORES")
        print("#"*40 + "\n")

        scores = self.load_records()
        if not scores:
            print("No scores yet.Be the first hero to win!")

        else:
            scores = sorted(scores,key = lambda x:x['scores'],reverse=True)
            for k, v in enumerate(scores[:10],1):
                print(f"{k}. {v['name']} | Scores: {v['scores']} | Level: {v['level']} | Status: {v['status']}")

        print("#"*40 + "\n")







