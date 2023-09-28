from datetime import datetime, timedelta

def color_date(date_string):
    if not date_string:
        return "gray"
    if isinstance(date_string, list):
        date_string = date_string[0]
    if isinstance(date_string, str):
        date = datetime.strptime(date_string, '%Y-%m-%d')
    else:
        date = date_string
    now = datetime.now()
    delta = now - date
    if delta.days > 90:
        return 'green'
    elif delta.days > 30:
        return 'orange'
    else:
        return 'red'



def text_date(date_string):
    if not date_string:
        return "Unknown"
    if isinstance(date_string, list):
        date_string = date_string[0]
    if isinstance(date_string, str):
        date = datetime.strptime(date_string, '%Y-%m-%d')
    else:
        date = date_string
    now = datetime.now()
    delta = now - date
    if delta.days > 90:
        return 'Sicher'
    elif delta.days > 30:
        return 'Risikoreich'
    else:
        return 'Unsicher'


def expl_date(date_string):
    if not date_string:
        return "Information about the creation date is not available."
    if isinstance(date_string, list):
        date_string = date_string[0]
    if isinstance(date_string, str):
        date = datetime.strptime(date_string, '%Y-%m-%d')
    else:
        date = date_string
    now = datetime.now()
    delta = now - date
    if delta.days > 90:
        return 'Wenn Sie sich Sorgen um Sicherheit beim Verwenden von Websites machen, werden Sie sich freuen zu wissen, dass diese Seite dies ernst nimmt. Eine der Hauptmethoden besteht darin, HTTPS-Verschlüsselung zu verwenden, was bedeutet, dass alle von Ihnen eingegebenen Daten auf der Website verschlüsselt sind und vor dem Abfangen durch Dritte geschützt sind. Die Website verwendet auch starke Passwortanforderungen und eine Zwei-Faktor-Authentifizierung, um sicherzustellen, dass nur autorisierte Benutzer auf sensible Informationen zugreifen können.'
    elif delta.days > 30:
        return 'Wenn Sie sich um Sicherheit beim Verwenden von Websites sorgen, sollten Sie wissen, dass diese Seite nur mittelmäßige Sicherheitsmaßnahmen zu haben scheint. Obwohl die Seite HTTPS verwendet, sind die Passwortanforderungen eher schwach, und es gibt keine Zwei-Faktor-Authentifizierung. Darüber hinaus scheint die Seite keine regelmäßigen Sicherheitsaudits durchzuführen oder ihre Software zu aktualisieren, um bekannte Schwachstellen zu beheben. Während es keine offensichtlichen Hinweise darauf gibt, dass die Website unsicher ist, gibt es auch keine besonderen Anstrengungen, um die Sicherheit zu gewährleisten.'
    else:
        return 'Wenn Sie diese Website besuchen, sollten Sie äußerst vorsichtig sein, da es viele Anzeichen dafür gibt, dass es sich um eine unsichere und schlechte Website handelt. Die Seite verwendet keine HTTPS-Verschlüsselung, was bedeutet, dass alle Daten, die Sie eingeben, von Dritten abgefangen werden können. Darüber hinaus sind die Passwortanforderungen sehr schwach oder gar nicht vorhanden, was bedeutet, dass Ihre Konten leicht gehackt werden könnten. Die Seite enthält auch viele Pop-ups und Anzeigen, die Sie auf verdächtige oder unerwünschte Websites weiterleiten könnten. Schließlich scheint die Seite keine klare Datenschutzrichtlinie oder Nutzungsbedingungen zu haben, was bedeutet, dass es unklar ist, was mit Ihren Daten geschieht, wenn Sie sie auf der Website eingeben. Zusammenfassend ist diese Website äußerst verdächtig und sollte vermieden werden, um Ihre Sicherheit zu gewährleisten.'



def get_creation_date_info(w):
    if 'Registered On:' in w:
        creation_date_color = color_date(w['Registered On:'])
        creation_date_text = text_date(w['Registered On:'])
        creation_date_expl = expl_date(w['Registered On:'])
    else:
        creation_date_color = "gray"
        creation_date_text = "Unknown"
        creation_date_expl = "Information about the creation date is not available."

    return creation_date_color, creation_date_text, creation_date_expl