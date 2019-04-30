import React, { Component } from 'react';
import { Card } from 'react-bootstrap';
import Ec from '../../components/Ec';
import jsonTimeNumber from '../../data/consumption/csp_time_num.json';
import jsonTimesMoney from '../../data/consumption/csp_times_money.json';
import jsonDateGender from '../../data/consumption/csp_date_gender.json';

const colors = [
    '#df6b66',
    '#749aa0',
    '#e79d88',
    '#8cc1aa',
    '#ec7e55',
    '#72a375',
    '#efdd7d',
    '#7189aa',
    '#cd5b58',
];

const getTimeData = (oriData, type) => {
    let res = [];
    if (type === 'am') {
        for (let i = 0; i < oriData.length; i ++) {
            if (oriData[i][1] < 24) {
                oriData[i][0] -= 1;
                res.push(oriData[i]);
            }
        }
    }
    if (type === 'pm') {
        for (let i = 0; i < oriData.length; i ++) {
            if (oriData[i][1] >= 24) {
                oriData[i][0] -= 1;
                res.push(oriData[i]);
            }
        }
    }
    return res;
};

const renderItemForTimeNum = (params, api) => {
    const values = [api.value(0), api.value(1)];
    const coord = api.coord(values);
    const size = api.size([1, 1], values);
    return {
        type: 'sector',
        shape: {
            cx: params.coordSys.cx,
            cy: params.coordSys.cy,
            r0: coord[2] - size[0] / 2,
            r: coord[2] + size[0] / 2,
            startAngle: -(coord[3] + size[1] / 1000),
            endAngle: -(coord[3] - size[1] / 1)
        },
        style: api.style({
            fill: api.visual('color')
        }),
        styleEmphasis: api.styleEmphasis()
    };
};

const getDiffType = (oriData, type) => {
    let res = [];
    let numMap = [[0, 100], [100, 500], [500, 1000], [1000, 2000]];
    if (type === 0) {
        for (let i = 6; i < oriData.length; i ++) {
            const sum = oriData[i][1] + oriData[i][2];
            if (oriData[i][3] < 6 && sum > numMap[type][0] && sum < numMap[type][1]) {
                res.push([oriData[i][0], sum]);
            }
        }
    } else {
        for (let i = 6; i < oriData.length; i ++) {
            const sum = oriData[i][1] + oriData[i][2];
            if (sum > numMap[type][0] && sum < numMap[type][1]) {
                res.push([oriData[i][0], sum]);
            }
        }
    }
    return res;
};

const clockOption= {
    legend: {
        bottom: 'bottom',
        data: ['上午AM', '下午PM'],
        selectedMode: 'single',
    },
    polar: {},
    tooltip: {
        formatter: (params) => {
            return '第' + (params.data[0] + 1) + '周<br />消费人数: ' + params.data[2];
        },
    },
    visualMap: {
        show: false,
        type: 'continuous',
        min: 0,
        max: 5000,
        range: [1, 5000],
        inRange: {
            color: ['#fff5f5', colors[0]],
        },
        outOfRange: {
            color: '#ffffff'
        }
    },
    angleAxis: {
        type: 'category',
        data: ['12', '', '1', '', '2', '', '3', '', '4', '','5','', '6', '', '7', '', '8', '', '9', '', '10', '', '11', ''],
        boundaryGap: false,
    },
    radiusAxis: {
        show: false,
        type: 'category',
        data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
    },
    series: [{
        name: '上午AM',
        type: 'custom',
        coordinateSystem: 'polar',
        legendHoverLink: false,
        itemStyle: {
            normal: {
                color: colors[0]
            },
            emphasis: {
                color: colors[1]
            },
        },
        renderItem: renderItemForTimeNum,
        data: getTimeData(jsonTimeNumber.data, 'am'),
    }, {
        name: '下午PM',
        type: 'custom',
        coordinateSystem: 'polar',
        itemStyle: {
            normal: {
                color: colors[0]
            },
            emphasis: {
                color: colors[1]
            },
        },
        renderItem: renderItemForTimeNum,
        data: getTimeData(jsonTimeNumber.data, 'pm'),

    }]
};

const riverOption = {
    color: [colors[0], colors[1]],
    tooltip: {
        trigger: 'axis',
        formatter: (params) => {
            return params[0].data[0] + '<br/>' +
                params[0].marker + params[0].data[2] + '消费: ' + params[0].data[1].toFixed(2) + '元<br/>' +
                params[1].marker + params[1].data[2] + '消费: ' + params[1].data[1].toFixed(2) + '元';
        },
        axisPointer: {
            type: 'line',
            lineStyle: {
                color: 'rgba(0,0,0,0.2)',
                width: 1,
                type: 'solid'
            }
        }
    },
    legend: {
        data: ['男生', '女生']
    },
    singleAxis: {
        top: 50,
        bottom: 50,
        axisTick: {},
        axisLabel: {},
        type: 'time',
        axisPointer: {
            animation: true,
            label: {
                show: true
            }
        },
        splitLine: {
            show: false,
        }
    },
    series: [
        {
            type: 'themeRiver',
            label: {
                show: false,
            },
            data: (function(oriData) {
                let res = [];
                for (let i = 6; i < oriData.length; i ++) {
                    if (oriData[i][3] < 6) {
                        res.push([oriData[i][0], oriData[i][4], '男生']);
                        res.push([oriData[i][0], oriData[i][5], '女生']);
                    }
                }
                return res;
            })(jsonDateGender.data),
        }
    ]
};

const calendarOption = {
    legend: {
        top: 'top',
        data: ['消费人数', '人均消费金额'],
    },
    tooltip: {
        formatter: (params) => {
            const unit = params.seriesIndex? '元' : '人';
            return params.value[0] + '<br/>' +
                params.marker + params.seriesName + ': ' + params.value[1].toFixed(2) + unit;
        }
    },
    visualMap: [{
        min: 0,
        max: 2000,
        right: 'right',
        bottom: 'bottom',
        itemHeight: 100,
        calculable: true,
        seriesIndex: [0],
        inRange: {
            opacity: [0.2, 0.6],
            color: colors[1]
        },
    }, {
        min: 0,
        max: 35,
        range: [8, 30],
        right: 'right',
        top: 'top',
        itemHeight: 100,
        calculable: true,
        inRange: {
            color: colors[0],
        },
        outOfRange: {
            color: '#e83015',
        },
        seriesIndex: [1],
    }],
    calendar: {
        cellSize: [32, 32],
        range: ['2018/08/01','2019/01/30'],
        splitLine: {
            lineStyle: {
                width: 1.5,
                opacity: 0.5,
            }
        },
        itemStyle: {
            normal: {borderWidth: 0.5}
        },
        dayLabel: {
            nameMap: 'cn',
        },
        monthLabel: {
            nameMap: 'cn',
        },
    },
    series: [{
        name: '消费人数',
        type: 'heatmap',
        coordinateSystem: 'calendar',
        itemStyle: {
            color: colors[1],
            emphasis: {
                shadowBlur: 5,
                shadowColor: '#898989'
            }
        },
        data: (function (oriData) {
            let res = [];
            for (let i = 6; i < oriData.length; i ++) {
                res.push([oriData[i][0], oriData[i][1] + oriData[i][2]])
            }
            return res;
        })(jsonDateGender.data),
    }, {
        name: '人均消费金额',
        type: 'scatter',
        coordinateSystem: 'calendar',
        legendHoverLink: false,
        data: (function (oriData) {
            let res = [];
            for (let i = 6; i < oriData.length; i ++) {
                const avg = (oriData[i][4] + oriData[i][5]) / (oriData[i][1] + oriData[i][2]);
                if (avg <= 30) {
                res.push([oriData[i][0], avg]);
                } else {
                    res.push([oriData[i][0], avg, 27]);
                }
            }
            return res;
        })(jsonDateGender.data),
        symbolSize: function (val) {
            if (val[2]) {
                return val[2];
            }
            return val[1]/1.5;
        },
        itemStyle: {
            normal: {
                color: colors[0],
            }
        }
    }]
};

const peoNumDateOption = {
    color: ['#e83015', colors[5], colors[4], colors[1]],
    legend: {
        data: ['异常', '区间1', '区间2', '区间3'],
        align: 'left'
    },
    tooltip: {
        trigger: 'axis',
        formatter: (params) => {
            return params[0].data[0] + '<br/>' + params[0].marker + params[0].data[1] + '人';
        },
        axisPointer: {
            type: 'line',
            lineStyle: {
                color: 'rgba(0,0,0,0.2)',
                width: 1,
                type: 'solid'
            }
        }
    },
    xAxis: {
        type: 'time',
        silent: false,
        splitLine: {
            show: false
        }
    },
    yAxis: {
        name: '消费人数/人',
    },
    series: [{
        name: '异常',
        type: 'scatter',
        data: getDiffType(jsonDateGender.data, 0),

    }, {
        name: '区间1',
        type: 'line',
        data: getDiffType(jsonDateGender.data, 1),
    }, {
        name: '区间2',
        type: 'line',
        data: getDiffType(jsonDateGender.data, 2),
    }, {
        name: '区间3',
        type: 'line',
        markPoint: {
            data: [
                {type: 'max', name: '最大值'},
            ]
        },
        markLine: {
            data: [
                {type: 'average', name: '平均值'}
            ]
        },
        data: getDiffType(jsonDateGender.data, 3),
    }],
};

const setGrid = () => {
    const gridWidth = '37%';
    const gridHeight = '37%';
    const gridLeft = 85;
    const gridRight = 85;
    const gridTop = 30;
    const gridBottom = 50;
    return [{
        id: 'xAxisLeft-yAxisTop',
        left: gridLeft,
        top: gridTop,
        width: gridWidth,
        height: gridHeight
    }, {
        id: 'xAxisLeft-yAxisBottom',
        left: gridLeft,
        bottom: gridBottom,
        width: gridWidth,
        height: gridHeight
    }, {
        id: 'xAxisRight-yAxisTop',
        right: gridRight,
        top: gridTop,
        width: gridWidth,
        height: gridHeight
    }, {
        id: 'xAxisRight-yAxisBottom',
        right: gridRight,
        bottom: gridBottom,
        width: gridWidth,
        height: gridHeight
    }];
};

const makeAxis = (id, name, nameLocation) => {
    return {
        id: id,
        name: name,
        nameLocation: nameLocation,
        nameGap: nameLocation === 'middle' ? 30 : 10,
        gridId: id,
        splitLine: {show: false},
    };
};

const makeSeries = (xPosition, yPosition, oriData, d1, d2) => {
    const id = xPosition+ '-' + yPosition;
    let xMin, yMin, xMax, yMax;
    // 规定贫困范围及异常范围
    if (d1 === 0) {  // x为消费次数
        xMin = 50;
        xMax = 650;
    } else { // x为平均消费
        xMin = 8;
        xMax = 20;
    }
    if (d2 === 1) {  // y为总额
        yMin = 1000;
        yMax = 5500;
    } else {  // y为平均消费
        yMin = 8;
        yMax = 20;
    }
    return {
        type: 'scatter',
        xAxisId: id,
        yAxisId: id,
        animationThreshold: 5000,
        progressiveThreshold: 5000,
        data: getData(oriData, d1, d2, xMin, yMin, xMax, yMax),
    };
};

const getData = (oriData, d1, d2, xMin, yMin, xMax, yMax) => {
    let res = [];
    for (let i = 6; i < oriData.length; i ++) {
        let type = 0;
        const x = oriData[i][d1];
        const y = oriData[i][d2];
        if (x <= xMin && y <= yMin) {
            type = 1;
        }
        if (x > xMax || y > yMax) {
            type = 2;
        }
        res.push([x, y, type]);
    }
    return res;
};

const getVisualMap = (index) => {
    return {
        show: false,
        seriesIndex: index,
        pieces: [
            {value: 0, color: colors[1]},
            {value: 1, color: colors[6]},
            {value: 2, color: '#e83015'},

        ],
        dimension: 2
    };
};

const featureOption = {
    color: colors[8],
    grid: setGrid(),
    xAxis: [
        makeAxis('xAxisLeft-yAxisTop', '消费次数', 'middle'),
        makeAxis('xAxisLeft-yAxisBottom', '消费次数', 'middle'),
        makeAxis('xAxisRight-yAxisTop', '平均消费金额', 'middle'),
        // makeAxis('xAxisRight-yAxisBottom', 'potassium', 'middle')
    ],
    yAxis: [
        makeAxis('xAxisLeft-yAxisTop', '消费总额', 'end'),
        makeAxis('xAxisLeft-yAxisBottom', '平均消费金额', 'end'),
        makeAxis('xAxisRight-yAxisTop', '消费总额', 'end'),
        // makeAxis('xAxisRight-yAxisBottom', 'fiber', 'end')
    ],
    visualMap: [
        getVisualMap(0),
        getVisualMap(1),
        getVisualMap(2),
    ],
    axisPointer: {
        show: true,
        snap: true,
        lineStyle: {
            type: 'dashed'
        },
        label: {
            show: true,
            margin: 6,
            backgroundColor: '#556',
            textStyle: {
                color: '#fff'
            }
        },
        link: [{
            xAxisId: ['xAxisLeft-yAxisTop', 'xAxisLeft-yAxisBottom']
        }, {
            yAxisId: ['xAxisLeft-yAxisTop', 'xAxisRight-yAxisTop']
        }]
    },
    series: [
        makeSeries('xAxisLeft', 'yAxisTop', jsonTimesMoney.data, 0, 1),
        makeSeries('xAxisLeft', 'yAxisBottom', jsonTimesMoney.data, 0, 2),
        makeSeries('xAxisRight', 'yAxisTop', jsonTimesMoney.data, 2, 1),
        // makeSeries('xAxisRight', 'yAxisBottom')
    ]
};

export default class extends Component {
    render() {
        return (
            <React.Fragment>
                <div className="row mb-lg-4">
                    <div className="col-12 col-lg-8">
                        <Card>
                            <Card.Header>
                                <span className="badge badge-info float-right">趋势图</span>
                                <h5 className='card-title mb-0'>区间消费人数情况</h5>
                            </Card.Header>
                            <Card.Body>
                                <Ec option={peoNumDateOption} h='360px'/>
                            </Card.Body>
                        </Card>
                    </div>
                    <div className="col-12 col-lg-4">
                        <Card>
                            <Card.Header>
                                <span className="badge badge-danger float-right">高峰预警</span>
                                <h5 className='card-title mb-0'>24小时消费人数分布</h5>
                            </Card.Header>
                            <Card.Body>
                                <Ec option={clockOption} h='360px'/>
                            </Card.Body>
                        </Card>
                    </div>
                </div>
                <div className="row mb-lg-4">
                    <div className="col-lg">
                        <Card>
                            <Card.Header>
                                <span className="badge badge-info float-right">趋势图</span>
                                <h5 className='card-title mb-0'>消费总金额变化趋势</h5>
                            </Card.Header>
                            <Card.Body>
                                <Ec option={riverOption} h='400px'/>
                            </Card.Body>
                        </Card>
                    </div>
                </div>
                <div className="row mb-lg-4">
                    <div className="col-lg">
                        <Card>
                            <Card.Header>
                                <span className="badge badge-danger float-right">消费预警</span>
                                <h5 className='card-title mb-0'>消费总览</h5>
                            </Card.Header>
                            <Card.Body>
                                <Ec option={calendarOption} h='300px'/>
                            </Card.Body>
                        </Card>
                    </div>
                </div>
                <div className="row">
                    <div className="col-lg">
                        <Card>
                            <Card.Header>
                                <span className="badge badge-danger float-right">异常预警</span>
                                <h5 className='card-title mb-0'>学生消费分布</h5>
                            </Card.Header>
                            <Card.Body>
                                <Ec option={featureOption} h='640px'/>
                            </Card.Body>
                        </Card>
                    </div>
                </div>
            </React.Fragment>
        );
    }
}
