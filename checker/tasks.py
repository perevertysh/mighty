from datetime import datetime
from typing import Tuple

from mighty.celery import app

from .models import Answer, AnswerStatus
from .grader import post_submission, get_submission


@app.task
def add(a, b):
    return a + b


@app.task
def push_answer(answer: str) -> [int] or [str]:
    time_stamp = datetime.now()
    check_id, status = post_submission(answer)
    ans = Answer(
        answer=answer,
        check_id=check_id,
        status=AnswerStatus.objects.get(code=status),
        created_time=time_stamp
    )
    ans.save()
    if ans.status.code != "evaluation":
        return ans.status.name
    return check_id


@app.task
def check_answer(id: int) -> Tuple[int, str]:
    check_id, status = get_submission(id)
    if status != "evaluation":
        ans = Answer.objects.get(check_id=check_id)
        ans.status = AnswerStatus.objects.get(code=status)
        ans.save()
        return ans.status.name
    return check_id
