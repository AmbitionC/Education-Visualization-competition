function data_visualization1() {

    var myChart = echarts.init(document.getElementById('visual-1'));

    var option = {
        title: {
            text: "学科—师资分配情况",
            left: 'left'
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['高一', '高二', '高三']
        },
        xAxis: {
            name: '学科',
            type: 'category',
            data: ['语文', '数学', '英语', '物理', '化学', '政治', '历史', '生物', '地理', '技术', '美术',
                '体育', '音乐']
        },
        yAxis: {
            name: '人数',
            type: 'value'
        },
        toolbox: {
            feature: {
                dataView: {show: true, readOnly: false},
                magicType: {show: true, type: ['line', 'stack']},
                restore: {show: true},
                saveAsImage: {show: true}
            }
        },
        series: [
            {
                name: '高一',
                type: 'bar',
                itemStyle: {
                    color: '#ff9797',
                },
                label: {
                    normal: {
                        show: false,
                        position: 'insideTop'
                    }
                },
                data: [24, 27, 47, 19, 18, 10, 9, 12, 11, 1, 3, 1, 2]
            },
            {
                name: '高二',
                type: 'bar',
                itemStyle: {
                    color:  '#b3d9d9',
                },
                label: {
                    normal: {
                        show: false,
                        position: 'insideTop'
                    }
                },
                data: [22, 24, 40, 11, 8, 8, 4, 11, 4, 9, 3, 1, 2]
            },
            {
                name: '高三',
                type: 'bar',
                itemStyle: {
                    color: '#adadad',
                },
                label: {
                    normal: {
                        show: false,
                        position: 'insideTop'
                    }
                },
                data: [21, 20, 32, 9, 10, 4, 4, 8, 4, 6, 2, 1, 2]
            },
        ]
    };

    myChart.setOption(option);
}

function data_visualization2() {
    var myChart = echarts.init(document.getElementById('visual-2'));


    var option = {
        title: {
            text: "教师带班数量一览表",
            left: 'left'
        },
        tooltip :{
            formatter: function (params) {
                return [
                    '教师：' + params.data[0],
                    '带班数：' + params.data[1]
                ].join('<br/>')
            }
        },

        xAxis: {
            name: '教师名',
            type: 'category',
            min: 'dataMin',
            max: 'dataMax'
        },
        yAxis: {
            name: '班级数',
            type: 'value',
        },
        series: [
            {
                type: 'bar',
                data: []
            }
        ]
    };

    $.get('./Dataset/School_Teacher_1.json').done(function (data) {
        $('#selectSub').on('change', function () {
            data_change();
            draw();
        });

        function name_change() {
            let namex = $('#selectSub').val();
            let name_apply = data.name[namex];
            return name_apply
        }

        function data_change() {
            let datax = $('#selectSub').val();
            let data_apply = data.row[datax];
            return data_apply
        }

        function color_change() {
            let color = ['#ff9797','#b3d9d9', '#adadad', '#d48265', '#91c7ae','#749f83',  '#ca8622', '#bda29a','#6e7074', '#546570', '#c4ccd3'];
            let colorx = $('#selectSub').val();
            let color_apply = color[colorx];
            return color_apply

        }

        function draw() {
            let dataset = data_change();
            let nameset = name_change();
            let colorset = color_change();
            myChart.setOption({
                xAxis: {
                    data: nameset
                },
                series: [{
                    data: dataset,
                    itemStyle: {
                        color: colorset
                    }
                }]
            })
        }

    draw();
    });

    myChart.setOption(option);
}

function data_visualization3() {
    var myChart = echarts.init(document.getElementById('visual-3'));
    myChart.showLoading();

    var data1 = {
        "name": "效实中学",
        "children": [
            {
                "name": "语文",
                "children": [
                    {'name': '虞老师', 'value': 16},
                    {'name': '蒋老师', 'value': 11},
                    {'name': '傅老师', 'value': 10},
                    {'name': '谢老师', 'value': 12}, {'name': '顾老师', 'value': 7}, {'name': '陈老师', 'value': 18}, {'name': '唐老师', 'value': 19}, {'name': '洪老师', 'value': 16}, {'name': '张老师', 'value': 18}, {'name': '张老师', 'value': 9}, {'name': '蒋老师', 'value': 18}, {'name': '岑老师', 'value': 15}, {'name': '黄老师', 'value': 13}, {'name': '陈老师', 'value': 10}, {'name': '郑老师', 'value': 14}, {'name': '徐老师', 'value': 9}, {'name': '孙老师', 'value': 3}, {'name': '叶老师', 'value': 9}, {'name': '杜老师', 'value': 23}, {'name': '朱老师', 'value': 17}, {'name': '马老师', 'value': 18}, {'name': '刘老师', 'value': 18}, {'name': '王老师', 'value': 1}, {'name': '潘老师', 'value': 1}, {'name': '张老师', 'value': 4}, {'name': '周老师', 'value': 4}, {'name': '李老师', 'value': 1}]

            },
            {
                "name": "数学",
                "children":[{'name': '胡老师', 'value': 5}, {'name': '李老师', 'value': 8}, {'name': '贾老师', 'value': 17}, {'name': '黄老师', 'value': 10}, {'name': '戴老师', 'value': 9}, {'name': '牟老师', 'value': 14}, {'name': '杨老师', 'value': 17}, {'name': '朱老师', 'value': 16}, {'name': '潘老师', 'value': 18}, {'name': '杜老师', 'value': 15}, {'name': '张老师', 'value': 6}, {'name': '胡老师', 'value': 10}, {'name': '童老师', 'value': 18}, {'name': '吕老师', 'value': 18}, {'name': '张老师', 'value': 9}, {'name': '郑老师', 'value': 14}, {'name': '周老师', 'value': 17}, {'name': '翁老师', 'value': 2}, {'name': '闵老师', 'value': 11}, {'name': '梁老师', 'value': 3}, {'name': '邬老师', 'value': 15}, {'name': '鲍老师', 'value': 1}, {'name': '范老师', 'value': 9}, {'name': '鲁老师', 'value': 14}, {'name': '吕老师', 'value': 4}, {'name': '沈老师', 'value': 2}, {'name': '周老师', 'value': 1}, {'name': '张老师', 'value': 2}, {'name': '周老师', 'value': 2}, {'name': '朱老师', 'value': 2}, {'name': '胡老师', 'value': 1}]

            },
            {
                "name": "英语",
                "children": [{'name': '周老师', 'value': 13}, {'name': '程老师', 'value': 11}, {'name': '陈老师', 'value': 6}, {'name': '王老师', 'value': 12}, {'name': '袁老师', 'value': 10}, {'name': '周老师', 'value': 10}, {'name': '曹老师', 'value': 10}, {'name': '陈老师', 'value': 11}, {'name': '沈老师', 'value': 9}, {'name': '朱老师', 'value': 12}, {'name': '吴老师', 'value': 13}, {'name': '王老师', 'value': 13}, {'name': '何老师', 'value': 19}, {'name': '赵老师', 'value': 6}, {'name': '王老师', 'value': 15}, {'name': '戴老师', 'value': 4}, {'name': '周老师', 'value': 12}, {'name': '武老师', 'value': 14}, {'name': '王老师', 'value': 11}, {'name': '陈老师', 'value': 13}, {'name': '高老师', 'value': 7}, {'name': '陈老师', 'value': 10}, {'name': '张老师', 'value': 11}, {'name': '郑老师', 'value': 10}, {'name': '周老师', 'value': 8}, {'name': '何老师', 'value': 14}, {'name': '郑老师', 'value': 10}, {'name': '李老师', 'value': 7}, {'name': '王老师', 'value': 11}, {'name': '毕老师', 'value': 1}, {'name': '徐老师', 'value': 13}, {'name': '王老师', 'value': 3}, {'name': '王老师', 'value': 1}, {'name': '牟老师', 'value': 1}, {'name': '熊老师', 'value': 2}, {'name': '夏老师', 'value': 2}, {'name': '李老师', 'value': 1}]

            },
            {
                "name": "物理",
                "children": [
                    {"name": "张老师", "value": 8833},
                    {"name": "汪老师", "value": 1732}
                ]
            },
            {
                "name": "化学",
                "children": [
                    {"name": "张老师", "value": 8833},
                    {"name": "汪老师", "value": 1732}
                ]
            },
            {
                "name": "政治",
                "children": [
                    {"name": "张老师", "value": 8833},
                    {"name": "汪老师", "value": 1732}
                ]
            },
            {
                "name": "历史",
                "children": [
                    {"name": "张老师", "value": 8833},
                    {"name": "汪老师", "value": 1732}
                ]
            },
            {
                "name": "生物",
                "children": [
                    {"name": "张老师", "value": 8833},
                    {"name": "汪老师", "value": 1732}
                ]
            },
            {
                "name": "地理",
                "children": [
                    {"name": "张老师", "value": 8833},
                    {"name": "汪老师", "value": 1732}
                ]
            },
            {
                "name": "技术",
                "children": [
                    {"name": "张老师", "value": 8833},
                    {"name": "汪老师", "value": 1732}
                ]
            },
            {
                "name": "美术",
                "children": [
                    {"name": "张老师", "value": 8833},
                    {"name": "汪老师", "value": 1732}
                ]
            },
            {
                "name": "体育",
                "children": [
                    {"name": "张老师", "value": 8833},
                    {"name": "汪老师", "value": 1732}
                ]
            },
            {
                "name": "音乐",
                "children": [
                    {"name": "张老师", "value": 8833},
                    {"name": "汪老师", "value": 1732}
                ]
            },
        ]
    };

    var data2 = {
        "name": "flare",
        "children": [
            {
                "name": "flex",
                "children": [
                    {"name": "FlareVis", "value": 4116}
                ]
            },
            {
                "name": "scale",
                "children": [
                    {"name": "IScaleMap", "value": 2105},
                    {"name": "LinearScale", "value": 1316},
                    {"name": "LogScale", "value": 3151},
                    {"name": "OrdinalScale", "value": 3770},
                    {"name": "QuantileScale", "value": 2435},
                    {"name": "QuantitativeScale", "value": 4839},
                    {"name": "RootScale", "value": 1756},
                    {"name": "Scale", "value": 4268},
                    {"name": "ScaleType", "value": 1821},
                    {"name": "TimeScale", "value": 5833}
                ]
            },
            {
                "name": "display",
                "children": [
                    {"name": "DirtySprite", "value": 8833}
                ]
            }
        ]
    };

    myChart.hideLoading();

    myChart.setOption(option = {
        tooltip: {
            trigger: 'item',
            triggerOn: 'mousemove'
        },
        legend: {
            top: '2%',
            left: '3%',
            orient: 'vertical',
            data: [{
                name: 'tree1',
                icon: 'rectangle'
            } ,
                {
                    name: 'tree2',
                    icon: 'rectangle'
                }],
            borderColor: '#c23531'
        },
        series:[
            {
                type: 'tree',

                name: 'tree1',

                data: [data1],

                top: '5%',
                left: '7%',
                bottom: '2%',
                right: '60%',

                symbolSize: 7,

                label: {
                    normal: {
                        position: 'left',
                        verticalAlign: 'middle',
                        align: 'right'
                    }
                },

                leaves: {
                    label: {
                        normal: {
                            position: 'right',
                            verticalAlign: 'middle',
                            align: 'left'
                        }
                    }
                },

                expandAndCollapse: true,

                animationDuration: 550,
                animationDurationUpdate: 750

            },
            {
                type: 'tree',
                name: 'tree2',
                data: [data2],

                top: '20%',
                left: '60%',
                bottom: '22%',
                right: '18%',

                symbolSize: 7,

                label: {
                    normal: {
                        position: 'left',
                        verticalAlign: 'middle',
                        align: 'right'
                    }
                },

                leaves: {
                    label: {
                        normal: {
                            position: 'right',
                            verticalAlign: 'middle',
                            align: 'left'
                        }
                    }
                },

                expandAndCollapse: true,

                animationDuration: 550,
                animationDurationUpdate: 750
            }
        ]
    });

}
