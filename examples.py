import random

import simple

# Create a "pass" event that will get handled by the pass route
# >> Quarterback Patrick Mahomes completed a 37 yard pass to Travis Kelce
simple.execute(
    event={
        "route_key": "pass",
        "data": {
            "qb": "Patrick Mahomes",
            "player": "Travis Kelce",
            "yards": random.randint(1, 100),
        },
    }
)

# Create a "run" event that will get handled by the run route
# >> Quarterback Jalen Hurts handed the ball to Saquon Barkley who ran 93 yards for a touchdown
simple.execute(
    event={
        "route_key": "run",
        "data": {
            "qb": "Jalen Hurts",
            "player": "Saquon Barkley",
            "yards": random.randint(1, 100),
        },
    }
)

# Create an unhandled event that will result in a KeyError
# >> Error: 'Route key not found: fumble'
try:
    simple.execute(
        event={
            "route_key": "fumble",
            "data": {"qb": "Brett Favre"},
        }
    )
except KeyError as key_error:
    print(f"Error: {key_error}")
