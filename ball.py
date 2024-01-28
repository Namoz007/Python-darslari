class ball:
    def __init__(self,ball,subject,date) -> None:
        self.ball = ball
        self.subject = subject
        self.date = date

    def __str__(self) -> str:
        print(f"""
Ball {self.ball}
Subject {self.subject}
Date {self.date}
""")