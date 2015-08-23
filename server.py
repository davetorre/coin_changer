from bottle import route, run, template
from coin_changer import make_change_usd

@route('/change/<amount>')
def index(amount):
    change = make_change_usd(int(amount))
    return template('<b>Change for {{amount}}</b>'
                    '<p>Quarters: {{change.quarters}}</p>'
                    '<p>Dimes: {{change.dimes}}</p>'
                    '<p>Nickels: {{change.nickels}}</p>'
                    '<p>Pennies: {{change.pennies}}</p>',
                    change=change, amount=amount)

run(host='localhost', port=8080)
