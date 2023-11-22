import gym

from .warehouse import Action, ObserationType, RewardType, Warehouse

_sizes = {
    "tiny": (1, 3),
    "small": (2, 3),
    "medium": (2, 5),
    "large": (3, 5),
}

_difficulty = {"-easy": 2, "": 1, "-hard": 0.5}

# Doing one by one but can be made to be a loop later on.

# small-4ag
num_agents = 4
size = "small"
diff = ""
gym.register(
    id=f"rware-{size}-{num_agents}ag{diff}-v1",
    entry_point="rware.warehouse:Warehouse",
    kwargs={
        "column_height": 8,
        "shelf_rows": _sizes[size][0],
        "shelf_columns": _sizes[size][1],
        "n_agents": num_agents,
        "msg_bits": 0,
        "sensor_range": 1,
        "request_queue_size": int(num_agents * _difficulty[diff]),
        "max_inactivity_steps": None,
        "max_steps": 500,
        "reward_type": RewardType.INDIVIDUAL,
    },
)

# tiny-4ag
num_agents = 4
size = "tiny"
diff = ""
gym.register(
    id=f"rware-{size}-{num_agents}ag{diff}-v1",
    entry_point="rware.warehouse:Warehouse",
    kwargs={
        "column_height": 8,
        "shelf_rows": _sizes[size][0],
        "shelf_columns": _sizes[size][1],
        "n_agents": num_agents,
        "msg_bits": 0,
        "sensor_range": 1,
        "request_queue_size": int(num_agents * _difficulty[diff]),
        "max_inactivity_steps": None,
        "max_steps": 500,
        "reward_type": RewardType.INDIVIDUAL,
    },
)

# tiny-4ag-easy
num_agents = 4
size = "tiny"
diff = "easy"
gym.register(
    id=f"rware-{size}-{num_agents}ag{diff}-v1",
    entry_point="rware.warehouse:Warehouse",
    kwargs={
        "column_height": 8,
        "shelf_rows": _sizes[size][0],
        "shelf_columns": _sizes[size][1],
        "n_agents": num_agents,
        "msg_bits": 0,
        "sensor_range": 1,
        "request_queue_size": int(num_agents * _difficulty[diff]),
        "max_inactivity_steps": None,
        "max_steps": 500,
        "reward_type": RewardType.INDIVIDUAL,
    },
)

# tiny-2ag
num_agents = 2
size = "tiny"
diff = ""
gym.register(
    id=f"rware-{size}-{num_agents}ag{diff}-v1",
    entry_point="rware.warehouse:Warehouse",
    kwargs={
        "column_height": 8,
        "shelf_rows": _sizes[size][0],
        "shelf_columns": _sizes[size][1],
        "n_agents": num_agents,
        "msg_bits": 0,
        "sensor_range": 1,
        "request_queue_size": int(num_agents * _difficulty[diff]),
        "max_inactivity_steps": None,
        "max_steps": 500,
        "reward_type": RewardType.INDIVIDUAL,
    },
)
