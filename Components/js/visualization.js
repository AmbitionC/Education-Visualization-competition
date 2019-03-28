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
    $.getJSON('./Dataset/npmdepgraph.json', function (json) {
        myChart.hideLoading();
        myChart.setOption(option = {
            title: {
                text: 'NPM Dependencies'
            },
            animationDurationUpdate: 1500,
            animationEasingUpdate: 'quinticInOut',
            series : [
                {
                    type: 'graph',
                    layout: 'none',
                    // progressiveThreshold: 700,
                    data: json.nodes.map(function (node) {
                        return {
                            x: node.x,
                            y: node.y,
                            id: node.id,
                            name: node.label,
                            symbolSize: node.size,
                            itemStyle: {
                                normal: {
                                    color: node.color
                                }
                            }
                        };
                    }),
                    edges: json.edges.map(function (edge) {
                        return {
                            source: edge.sourceID,
                            target: edge.targetID
                        };
                    }),
                    label: {
                        emphasis: {
                            position: 'right',
                            show: true
                        }
                    },
                    roam: true,
                    focusNodeAdjacency: true,
                    lineStyle: {
                        normal: {
                            width: 0.5,
                            curveness: 0.3,
                            opacity: 0.7
                        }
                    }
                }
            ]
        }, true);
    });
    myChart.setOption(option);
}
