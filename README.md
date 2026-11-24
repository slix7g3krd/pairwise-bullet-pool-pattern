# pairwise-bullet-pool-pattern

## 领域

游戏、图形与多媒体

## 主题

弹幕对象池与轨迹重放

## 说明

取出复位、延迟回收与发射序确定性排序。

初始状态下 `gameplay/bullet_pool_pattern.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
