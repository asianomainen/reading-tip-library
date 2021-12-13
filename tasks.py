from invoke import task

@task
def start(ctx):
    ctx.run("poetry run invoke build")
    ctx.run("python3 src/index.py")

@task
def test(ctx):
    ctx.run("pytest src")

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")
@task
def coverage_report(ctx):
    ctx.run("coverage html")

@task
def build(ctx):
    ctx.run("python3 src/initialize_database.py")

@task
def robot(ctx):
    db = "robot.database.sqlite"
    ctx.run(f"DATABASE_FILENAME={db} robot src/tests/")

@task
def pylint(ctx):
    ctx.run("pylint src")