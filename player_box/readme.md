# box

> 一个不完善的随身箱子插件

## 依赖

- [MinecraftDataAPI](https://github.com/MCDReforged/MinecraftDataAPI)


## 指令


!!box 显示帮助信息  
!!box spawn 召唤你的箱子  
!!box store 存储你的箱子  
!!box tp <player> 将你的箱子送到别的玩家那  

逻辑：先召唤再存储，先召唤再tp（别没召唤就存储）

## 注意

- 可能存在刷运载矿车的bug
- 使用spawn会清除玩家身上运载矿车，可自行删除相关指令
- 有些时候玄学加载不成功，请重载

## 计划

已基本完成，目前主要进行 Bug 修复  
以下 TODO 优先级从高到低  

- [x]  更改玩家背包 ~~Mojang不让我改~~
- [ ]  修好刷运载矿车的bug
- [ ]  一些逻辑的优化
