from django import template

register = template.Library()

@register.filter(name='chunk')
def chunks(list,chunk_size):
    chunk = []
    i = 0
    for data in list:
        chunk.append(data)
        i = i+1
        if i==chunk_size:
            yield chunk
            chunk = []
    yield chunk
