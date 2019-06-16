import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';
import jsonDateGender from '../data/consumption/school/date_gender.json';

export default function() {
    const option = {
        legend: {
            top: 'top',
            data: ['消费人数', '消费总额'],
            selectedMode: 'single'
        },
        tooltip: {
            formatter: (params) => {
                const unit = params.seriesIndex? '元' : '人';
                return params.value[0] + '<br/>' +
                    params.marker + params.seriesName + ': ' + params.value[1].toFixed(2) + unit;
            }
        },
        visualMap: [{
            show: false,
            min: 0,
            max: 1650,
            range: [0, 1600],
            seriesIndex: [0],
            inRange: {
                opacity: [0.1, 0.9],
                color: '#749aa0'
            },
            outOfRange: {
                color: '#566c73',
            },
        }, {
            show: false,
            min: 0,
            max: 50000,
            range: [0, 45000],
            seriesIndex: [1],
            inRange: {
                opacity: [0.1, 0.9],
                color: '#df6b66',
            },
            outOfRange: {
                color: '#b54434',
            },
        }],
        calendar: {
            left: '4%',
            cellSize: 'auto',
            range: ['2018/07/01','2019/01/30'],
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
            yearLabel: {
                show: false,
            }
        },
        series: [{
            name: '消费人数',
            type: 'heatmap',
            coordinateSystem: 'calendar',
            itemStyle: {
                color: '#749aa0',
            },
            label: {
                normal: {
                    show: true,
                    formatter: (params) => {
                        return params.value[0].split('/')[2];
                    },
                    textStyle: {
                        fontSize: 12,
                        fontWeight: 500,
                        color: '#2b2b2b'
                    }
                }
            },
            data: (function (oriData) {
                let res = [];
                for (let i = 0; i < oriData.length; i ++) {
                    res.push([oriData[i][0], oriData[i][1] + oriData[i][2]])
                }
                return res;
            })(jsonDateGender.data),
        }, {
            name: '消费总额',
            type: 'heatmap',
            coordinateSystem: 'calendar',
            label: {
                normal: {
                    show: true,
                    formatter: (params) => {
                        return params.value[0].split('/')[2];
                    },
                    textStyle: {
                        fontSize: 12,
                        fontWeight: 500,
                        color: '#2b2b2b'
                    }
                }
            },
            data: (function (oriData) {
                let res = [];
                for (let i = 0; i < oriData.length; i ++) {
                    res.push([oriData[i][0], oriData[i][4] + oriData[i][5]]);
                }
                return res;
            })(jsonDateGender.data),
            itemStyle: {
                color: '#df6b66',
            }
        }]
    };
    return (
        <Card>
            <Card.Header>
                <h4>1-5-1 消费日历 / 2018-2019</h4>
            </Card.Header>
            <Card.Body>
                <Ec option={option} h='280px'/>
            </Card.Body>
        </Card>
    );
}