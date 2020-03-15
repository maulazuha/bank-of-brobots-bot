profile = '''query {{
    user(id: "{0}") {{
        name
        money
        planName
        planCost
        weekLeft
        weekLimit
        isAdmin
        transactions {{
            id
            money
            fromUser {{
                name
            }}
            toUser {{
                name
            }}
        }}
    }}
}}'''

transfer = '''mutation {{
    transfer(money: {}, from_user_id: "{}", to_user_id: "{}") {{
        id
    }}
}}'''

subscriptions = '''query {
    subscriptions {
        id
        name
        cost
        limit
    }
}'''

change_subscription = '''mutation {{
    changeSubscription(subscriptionId: {}, userId: "{}") {{
        name
    }}
}}'''
