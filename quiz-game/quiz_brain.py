class QuizBrain:

  def __init__(self, questions_list) -> None:
    self.question_number = 0
    self.correct_answers = 0
    self.questions_list = questions_list

  def still_has_questions(self):
    return self.question_number < len(self.questions_list)
  
  def handle_correct_answer(self):
    self.correct_answers += 1
    print("Correct!")
    print(f"Total: {self.correct_answers}/{self.question_number}")

  def handle_incorrect_answer(self):
    print("Incorrect")
    print(f"Total: {self.correct_answers}/{self.question_number}")

  def next_question(self):
    current_question = self.questions_list[self.question_number]
    self.question_number += 1
    user_input = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")

    if user_input.lower() == current_question.answer.lower():
      self.handle_correct_answer()
    else:
      self.handle_incorrect_answer()

    if self.still_has_questions():
      self.next_question()

