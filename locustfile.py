import random
import time

from locust import HttpUser, between, task


class ChatUser(HttpUser):
    wait_time = between(5, 20)

    @task
    def ask_question(self):
        self.client.get("/")
        time.sleep(5)
        self.client.post(
            "/chat",
            json={
                "history": [
                    {
                        "content": random.choice(
                            [
                                "What is CNF?",
                                "How do I troubleshoot mailbox provisioning issue?",
                                "What elevation do I need for Set-Mailbox?",
                                "Are there any similar incidents to incident 12345?",
                            ]
                        ),
                        "role": "user",
                    },
                ],
                "overrides": {
                    "retrieval_mode": "hybrid",
                    "semantic_ranker": True,
                    "semantic_captions": False,
                    "top": 3,
                    "suggest_followup_questions": False,
                },
            },
        )
        time.sleep(5)
        self.client.post(
            "/chat",
            json={
                "history": [
                    {"content": "What happens in a performance review?", "role": "user"},
                    {
                        "content": "During a performance review, employees will receive feedback on their performance over the past year, including both successes and areas for improvement. The feedback will be provided by the employee's supervisor and is intended to help the employee develop and grow in their role [employee_handbook-3.pdf]. The review is a two-way dialogue between the employee and their manager, so employees are encouraged to be honest and open during the process [employee_handbook-3.pdf]. The employee will also have the opportunity to discuss their goals and objectives for the upcoming year [employee_handbook-3.pdf]. A written summary of the performance review will be provided to the employee, which will include a rating of their performance, feedback, and goals and objectives for the upcoming year [employee_handbook-3.pdf].",
                        "role": "assistant",
                    },
                    {"content": "Does my plan cover eye exams?", "role": "user"},
                ],
                "overrides": {
                    "retrieval_mode": "hybrid",
                    "semantic_ranker": True,
                    "semantic_captions": False,
                    "top": 3,
                    "suggest_followup_questions": False,
                },
            },
        )
