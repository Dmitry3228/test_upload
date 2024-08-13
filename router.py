from fastapi import APIRouter, Depends

from repository import TaskRepository

from typing import Annotated

from schemas import Task, TaskAdd, TaskId


router = APIRouter(
    prefix= "/tasks",
    tags=["tasks"]
)


@router.post("")
async def create_task(
    task: Annotated[TaskAdd, Depends()]

) -> list[TaskId]:
    task_id = await TaskRepository.add_one(task)
    return {'ok': True, 'id': task_id}



@router.get("")
async def get_tasks() -> list[Task]:
    tasks = await TaskRepository.get_all()
    return {'data': tasks}