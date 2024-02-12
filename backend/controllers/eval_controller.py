from models.eval_model import Session, Evaluation


def add_evaluation(prompt, accuracy, faithfulness):
    session = Session()
    evaluation = Evaluation(prompt=prompt, accuracy=accuracy, faithfulness=faithfulness)
    session.add(evaluation)
    session.commit()
    session.close()
