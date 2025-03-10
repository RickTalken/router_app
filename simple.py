from routing import Router

router = Router()


@router.route("pass")
def handler(data: dict):
    """Handler for the 'pass' route"""
    qb = data.get("qb")
    player = data.get("player")
    yards = data.get("yards")
    print(f"Quarterback {qb} completed a {yards} yard pass to {player}")


@router.route("run")
def handler(data: dict):
    """Handler for the 'run' route"""
    qb = data.get("qb")
    player = data.get("player")
    yards = data.get("yards")
    print(
        f"Quarterback {qb} handed the ball to {player} who ran {yards} yards for a touchdown"
    )


def execute(event: dict):
    """Dispatch the event to a registered handler"""
    router.dispatch(event)
