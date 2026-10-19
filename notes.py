import click
import os
import config
import crud

@click.group()
@click.argument("filename")
def cli(filename):
    config.NOTES_FILE = os.path.join(os.getcwd(), filename)

@cli.command()
@click.argument("title")
@click.option("--content", help="The body of the note")
@click.option("--tags", help="Comma-separated tags")
def create(title, content, tags):
    success, message = crud.create_note(title, content, tags)
    click.echo(message)

@cli.command()
@click.argument("title")
def read(title):
    note = crud.read_note(title)
    
    if note:
        click.echo(f"Title: {title}")
        click.echo(f"Content: {note['content']}")
        click.echo(f"Tags: {', '.join(note['tags'])}")
    else:
        click.echo(f"Error: Note '{title}' not found.")

@cli.command()
@click.argument("title")
@click.option("--content", help="Updated body of the note")
@click.option("--tags", help="Updated comma-separated tags")
def update(title, content, tags):
    if not content and not tags:
        click.echo("Error: Please provide --content or --tags to update.")
        return
        
    success, message = crud.update_note(title, content, tags)
    click.echo(message)

@cli.command()
@click.argument("title")
def delete(title):
    success, message = crud.delete_note(title)
    click.echo(message)

@cli.command()
@click.option("--tag", help="Filter notes by tag")
@click.option("--keyword", help="Filter notes by a word in the content")
def show(tag, keyword):
    notes = crud.list_notes(tag, keyword)
    
    if not notes:
        click.echo("No notes found.")
        return
        
    for title, data in notes.items():
        click.echo(f"\n- {title}")
        click.echo(f"  Content: {data['content']}")
        if data['tags']:
            click.echo(f"  Tags: {', '.join(data['tags'])}")

if __name__ == "__main__":
    cli()