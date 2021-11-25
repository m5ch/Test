# ECharts {ignore}

[toc]

## 基本步骤

1. 引入echarts.min.js文件

    ```<script src = "路径"></script>```

2. 准备一个呈现图标的盒子

    ```<div id="main" style = "width: 600px; height: 400px;"></div>```

3. 初始echarts的实例对象

    ```var mychart = echarts.init(document.getElementById('main'));```

4. 准备配置项

    ```var option = {}```

5. 将配置项设置给echarts实例对象

    ```mychart.setOption(option);```

## ECharts常用图表


### 通用配置

1. 标题:title
- 文字样式

        textStyle:{},

- 标题边框

        borderWidth:,
        borderColor:'',
        borderRadius:,

- 标题位置

        left: ,
        right: ,
        top: ,
        bottom:

2. 提示:tooltip
提示框组件，用于配置鼠标滑过或点击图表时的显示框


- 触发类型

        tooltip:{
            trigger:'item'
            trigger:'axis'
        }

- 触发时机

        tooltip:{
            tirggerOn:'click'
            tirggerOn:'mousemove'
            tirggerOn:'mousemove|click'
        }

- 格式化

        tooltip:{
            formatter:
        }


3. 工具按钮:toolbox
Echarts提供的工具栏

- 内置有导出图片，数据视图，动态类型切换，数据区域缩放，重置五个工具

        toolbox:{
            feature:{
                saveAsImage:{},     //导出图片
                dataView:{},        //数据视图
                restore:{},         //重置
                dataZoom:{}         //区域缩放
                magicType:{
                    type:['bar','line']
                }                   //动态图表类型切换
            }
        }

4. 图例:legend
用于筛选系列，需要和series配合使用

legend中的data是一个数组
legend中的data值需要和series数组中某种数据的name值一致

        grid:{
            show:true,
            borderWidth:10,
            left:20,
            height:500,
            backgroungcolor:'',
        }


#### 直角坐标系中的常用配置

直角坐标系图表：柱状图、折线图。散点图

- 配置1：网格：grid
控制直角坐标系的布局和大小
x轴和y轴就是在grid的基础上绘制的


- 配置2：坐标轴：axis
xAxis和yAxis
一个grid最多有两种位置的x轴和y轴
- 坐标轴类型 type

    value:数值轴，自动会从目标数据中读取数据
    category类目轴，该类型必须通过data设置类目数据

- 显示位置


        xAxis:{
            position:'top'      // top bottom
        },
        yAxis:{
            position:'left'      // left right
        }


- 配置3：区域缩放：dataZoom
用于区域缩放，对数据范围过滤，x轴和y轴都可以拥有
dataZoom是一个数组，意味着可以可以配置多个区域缩放器
- 类型type
    option:{
        dataZoom[
            {
                type:'slider'   //滑块
                type:'inside'   //内置，鼠标滚轮或双指缩放

            },
        ],
    },

- 指明产生的作用轴
xAxisIndex:设置缩放组件控制的是哪个x轴，一般写0
yAxisIndex:设置缩放组件控制的是哪个y轴，一般写0

- 指明初始状态的缩放情况
start:数据缩放范围的起始百分比
end:数据缩放范围的结束百分比


        option:{
        dataZoom[
            {
                type:'slider'   //滑块
                type:'inside'   //内置，鼠标滚轮或双指缩放
                yAxisIndex: 0,
                start:20,
                end: 70
            },
        ],
    },





### 柱状图

1. 常见效果
- 标记：最大值、最小值、平均值
    ```
    markPoint:{
        data:[
        {
            type:"max",
            name:"最大值"
        },
        {
            type:"min",
            name:"最小值"
        }
    ],
    symbol:'pin'
    },
    markLine:{
        data:[
            {
                type:'average',
                name:'平均值'
            }
        ]
    },
    ```

- 显示：数值显示、柱宽度
    ```
    label:{
            show: true
            rotate:30
            position:
    },
    barWidth:'top'
    ```
- 横向柱状图
    x轴和y轴数据互换

### 折线图

> 通常用来分析数据随时间的变化趋势

1. 常见效果

- 标记：最大值、最小值、平均值、标注区间
    ```
    markPoint:{
        data:[
        {
            type:"max",
            name:"最大值"
        },
        {
            type:"min",
            name:"最小值"
        }
    ],
    symbol:'pin'
    },
    markLine:{
            data:[
                {
                    type:'average',
                    name:'平均值'
                }
            ]
        },
        markArea:{
            data: [
            [
                {
                    name: '平均值到最大值',
                    type: 'average'
                },
                {
                    type: 'max'
                }
            ], [
                {
                    name: '两个坐标之间的标域',
                    coord: [10, 20]
                },
                {
                    coord: [20, 30]
                }
            ], [
                {
                    name: '60分到80分',
                    yAxis: 60
                },
                {
                    yAxis: 80
                }
            ],
            [
                {
                    name: '7月到10月',
                    xAxis: '7月'
                },
                {
                    xAxis: '10月'
                }
            ], 
            [
                {
                    name: '所有数据范围区间',
                    coord: ['min', 'min']
                },
                {
                    coord: ['max', 'max']
                }
            ],
            [
                {
                    name: '两个屏幕坐标之间的标域',
                    x: 100,
                    y: 100
                }, {
                    x: '90%',
                    y: '10%'
                }
            ]
        ]
    }
    ```

- 线条控制:平滑、风格

        smooth:true,
        smooth:0.5,
        lineStyle:{
            color:,
            type:'',    //dashed dotted solid
        }

- 填充风格

        areaStyle:{

        }

- 紧挨边缘

        xAxis:{
            boundaryGap:false
        }

- 缩放：脱离0值比例

        yAxis:{
            scale:true
        }

- 堆叠图

        series:{
            stack:'all'
            areaStyle:{}
        }

### 散点图
可以帮助我们推断出变量之间的相关性，也经常用于地图的标注

1. 基本结构

> x轴和y轴的数据是一个二维数组
series中的type设置为scatter
xAxis和yAxis中的type设置为value


2. 常见效果
- 气泡图效果：大小、颜色

        symbolSize:function(arg){
            return 10
        }
        itemStyle:{
            color:function(arg){
                return 'red'
            }
        }
- 涟漪动画效果

        series:{
            //type:'scatter',
            type:'effcctScatter',
            showEffectOn:'emphasis',     //render  emphasis
            rippleEffect:{
                scale: 10
            },
        },

### 饼图
数据是字典类型

1. 常见效果
- 数值显示

        lable:{
            show:true,
            formatter:function(org){
                return 
            }
        }

- 圆环效果

        radius:40,      //饼图的半径
        radius:'20%',   //百分比参照的是宽度和高度中较小的那一部分的一半来进行百分比设置
        radius:['50%','75%'], //第0个是内圆，第1个是外圆

- 南丁格尔图

        roseType:'radius',      扇区圆心角展现数据的百分比，半径展现数据的大小。
        roseType:'area',        所有扇区圆心角相同，仅通过半径展现数据大小。

- 选中效果

        selectedMode:'single'
        selectedMode:'multiple'
        selectedOffset:10,

### 地图
1. 地图图表的使用方式
- 百度地图：需要申请百度地图ak
- 矢量地图：需要准备矢量地图数据



### 雷达图
### 仪表盘图

