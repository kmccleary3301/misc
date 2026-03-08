# Helper-mod artifact schemas

## Screenshot metadata example

```json
{
  "name": "config-screen-open",
  "dimension": "minecraft:overworld",
  "player": { "x": 10.5, "y": 64.0, "z": -3.5, "yaw": 180.0, "pitch": 8.0 },
  "held_item": "minecraft:stick",
  "target": { "type": "block", "id": "mymod:machine" },
  "screen": { "id": "mymod:config", "title": "My Mod Config" },
  "gui_scale": 3,
  "scene": "config-open",
  "world": "dev-smoke-world"
}
```

## State dump example

```json
{
  "dimension": "minecraft:overworld",
  "player": {
    "x": 10.5,
    "y": 64.0,
    "z": -3.5,
    "selected_slot": 0,
    "inventory": ["minecraft:stick", "mymod:machine"]
  },
  "target": { "type": "block", "id": "mymod:machine" },
  "screen": { "id": "mymod:config", "title": "My Mod Config" },
  "assertions": {
    "registries": ["mymod:machine"],
    "config_loaded": true
  }
}
```
