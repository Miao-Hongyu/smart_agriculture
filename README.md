# Smart Agriculture System - 温室自动灌溉与调温系统

## 项目简介
这是一个用于智慧农业的自动化温室管理系统。它通过传感器实时监测温室环境数据（温度、湿度、土壤湿度），并通过控制水泵、阀门和加热器等设备自动调节环境。该系统结合了AI决策模型，根据传感器数据决定是否需要灌溉、加热等。

## 环境要求
- Python 3.x
- 安装依赖库：在终端中运行
  ```bash
  pip install -r requirements.txt

## 项目结构 
 smart_agriculture/
  ├── config.py             # 配置文件：设置阈值、设备引脚等
  ├── sensors.py            # 传感器模块：读取温湿度、土壤湿度数据
  ├── actuators.py          # 执行器模块：控制水泵、电磁阀、加热器
  ├── ai_controller.py      # AI 模块：环境决策
  ├── ui.py                 # 用户界面模块：展示数据
  ├── dataset/
  │   ├── train_data.csv    # 训练数据集：环境参数（温度、湿度、土壤湿度）
  │   ├── test_data.csv     # 测试数据集
  ├── models/
  │   └── environment_model.h5  # TensorFlow 训练好的模型
  ├── main.py               # 主程序：整合所有模块
  ├── requirements.txt      # Python 依赖库
  └── README.md             # 项目使用说明

## 运行步骤
### 训练并保存 TensorFlow 模型
  python tensorflow.py
### 运行主程序
  python main.py

