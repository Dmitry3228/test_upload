from sqlalchemy import select
from database import TaskOrm, new_session
from schemas import Task, TaskAdd


class TaskRepository:
    @classmethod
    async def add_one(cls, data = TaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()
            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id


    @classmethod
    async def get_all(cls) -> list[Task]:
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            tasks_models = result.scalars().all()
            tasks_schema = [Task.model_validate(task) for task in tasks_models]
            return tasks_schema
