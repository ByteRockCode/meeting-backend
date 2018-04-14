# Motivo

{{ meeting.motive }}


# Asistentes
{% for guest in meeting.guests.all %}
- {{ guest }}
{% empty %}
No se registraron asistentes
{% endfor %}


# Acuerdos
{% for agreement in meeting.agreements.all %}
- {{ agreement.description }}
{% empty %}
No se registraron acuerdos
{% endfor %}


# Compromisos
{% for compromise in meeting.compromises.all %}
- {{ compromise.description }}
{% empty %}
No se registraron compromisos
{% endfor %}
