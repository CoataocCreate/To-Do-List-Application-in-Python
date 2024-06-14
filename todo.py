import click
import os

# File to store tasks
TODO_FILE = 'todo.txt'

@click.group()
def cli():
    pass

@cli.command()
@click.argument('task')
def add(task):
    """Add a new task"""
    with open(TODO_FILE, 'a') as f:
        f.write(task + '\n')
    click.echo(f'Added task: {task}')

@cli.command()
def list():
    """List all tasks"""
    if not os.path.exists(TODO_FILE):
        click.echo('No tasks added yet.')
    else:
        with open(TODO_FILE, 'r') as f:
            tasks = f.readlines()
            if tasks:
                click.echo('Tasks:')
                for idx, task in enumerate(tasks, start=1):
                    click.echo(f'{idx}. {task.strip()}')
            else:
                click.echo('No tasks added yet.')

@cli.command()
@click.argument('task_number', type=int)
def done(task_number):
    """Mark a task as done"""
    if not os.path.exists(TODO_FILE):
        click.echo('No tasks added yet.')
        return
    
    with open(TODO_FILE, 'r') as f:
        tasks = f.readlines()
    
    if task_number <= 0 or task_number > len(tasks):
        click.echo('Invalid task number.')
        return
    
    task_to_mark = tasks[task_number - 1].strip()
    
    with open(TODO_FILE, 'w') as f:
        for task in tasks:
            if task.strip() != task_to_mark:
                f.write(task)
    
    click.echo(f'Marked task "{task_to_mark}" as done.')

@cli.command()
@click.argument('task_number', type=int)
def delete(task_number):
    """Delete a task"""
    if not os.path.exists(TODO_FILE):
        click.echo('No tasks added yet.')
        return
    
    with open(TODO_FILE, 'r') as f:
        tasks = f.readlines()
    
    if task_number <= 0 or task_number > len(tasks):
        click.echo('Invalid task number.')
        return
    
    task_to_delete = tasks[task_number - 1].strip()
    
    with open(TODO_FILE, 'w') as f:
        for task in tasks:
            if task.strip() != task_to_delete:
                f.write(task)
    
    click.echo(f'Deleted task "{task_to_delete}".')

if __name__ == '__main__':
    if not os.path.exists(TODO_FILE):
        open(TODO_FILE, 'a').close()  # create an empty todo file if it doesn't exist
    cli()
