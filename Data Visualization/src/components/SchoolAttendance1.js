import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';
import Attendance1 from '../data/schoolAttendance/Attendance_1.json'
import Attendance2 from '../data/schoolAttendance/Attendance_2.json'
import Attendance3 from '../data/schoolAttendance/Attendance_3.json'
import Attendance4 from '../data/schoolAttendance/Attendance_4.json'

export default function() {
    const option = {
        tooltip: {
            formatter: function (params) {
                return [
                    params.data[0] + '的百分比为：' + params.data[1] + '%'
                ].join('<br/>')
            }
        },
        grid: {
            left: 0,
            right: '4%',
            top: '16%',
            bottom: 0,
            containLabel: true
        },
        legend: [{
            data: ['学年统计', '学期统计', '当前年份', '当前月份'],
            selectedMode: 'single',
            selected: {
                '学年统计': false,
                '学期统计': true,
            }
        }],
        xAxis: {
            name: '时间',
            type: 'category',
            max: 'dataMax',
            min: 'dataMin',
            axisTick: {
                show: false
            },
        },
        yAxis: {
            name: '百分比',
            type: 'value',
            max: 60,
            min: 'dataMin',
            axisLabel: {
                formatter: '{value}%'
            },
            axisTick: {
                show: false
            },
            splitLine: {
                lineStyle: {
                    color: '#eeeeee',
                    type: 'dashed'
                }
            }
        },
        series: [{
            data: Attendance1.late,
            name: '学年统计',
            type: 'line',
            smooth: true,
            itemStyle: {
                color: '#df6b66'
            },
            markPoint: {
                symbol: 'rect',
                symbolSize: [50, 25],
                data: [{
                    x: '96%',
                    y: 15,
                    value: '迟到晚到'
                }],
                silent: true
            },
            markLine: {
                data: [
                    {type: 'average', name: '平均值'}
                ],
                silent: true
            }
        },{
            data: Attendance1.early,
            name: '学年统计',
            type: 'line',
            smooth: true,
            itemStyle: {
                color:  '#71b9bc',
            },
            markPoint: {
                symbol: 'rect',
                symbolSize: [50, 25],
                data: [{
                    x: '96%',
                    y: 40,
                    value: '离校早退'
                }],
                silent: true
            },
            markLine: {
                data: [
                    {type: 'average', name: '平均值'}
                ],
                silent: true
            }
        },{
            data: Attendance1.uniform,
            name: '学年统计',
            type: 'line',
            smooth: true,
            itemStyle: {
                color: '#90ca8f',
            },
            markPoint: {
                symbol: 'rect',
                symbolSize: [50, 25],
                data: [{
                    x: '96%',
                    y: 65,
                    value: '校服校徽'
                }],
                silent: true
            },
            markLine: {
                data: [
                    {type: 'average', name: '平均值'}
                ],
                silent: true
            }
        },{
            data: Attendance2.late,
            name: '学期统计',
            type: 'line',
            smooth: true,
            itemStyle: {
                color: '#df6b66'
            },
            markPoint: {
                symbol: 'rect',
                symbolSize: [50, 25],
                data: [{
                    x: '96%',
                    y: 15,
                    value: '迟到晚到'
                }],
                silent: true
            },
            markLine: {
                data: [
                    {type: 'average', name: '平均值'}
                ],
                silent: true
            }
        },{
            data: Attendance2.early,
            name: '学期统计',
            type: 'line',
            smooth: true,
            itemStyle: {
                color:  '#71b9bc',
            },
            markPoint: {
                symbol: 'rect',
                symbolSize: [50, 25],
                data: [{
                    x: '96%',
                    y: 40,
                    value: '离校早退'
                }],
                silent: true
            },
            markLine: {
                data: [
                    {type: 'average', name: '平均值'}
                ],
                silent: true
            }
        },{
            data: Attendance2.uniform,
            name: '学期统计',
            type: 'line',
            smooth: true,
            itemStyle: {
                color: '#90ca8f',
            },
            markPoint: {
                symbol: 'rect',
                symbolSize: [50, 25],
                data: [{
                    x: '96%',
                    y: 65,
                    value: '校服校徽'
                }],
                silent: true
            },
            markLine: {
                data: [
                    {type: 'average', name: '平均值'}
                ],
                silent: true
            }
        },{
            data: Attendance3.late,
            name: '当前年份',
            type: 'line',
            smooth: true,
            itemStyle: {
                color: '#df6b66'
            },
            markPoint: {
                symbol: 'rect',
                symbolSize: [50, 25],
                data: [{
                    x: '96%',
                    y: 15,
                    value: '迟到晚到'
                }],
                silent: true
            },
            markLine: {
                data: [
                    {type: 'average', name: '平均值'}
                ],
                silent: true
            }
        },{
            data: Attendance3.early,
            name: '当前年份',
            type: 'line',
            smooth: true,
            itemStyle: {
                color:  '#71b9bc',
            },
            markPoint: {
                symbol: 'rect',
                symbolSize: [50, 25],
                data: [{
                    x: '96%',
                    y: 40,
                    value: '离校早退'
                }],
                silent: true
            },
            markLine: {
                data: [
                    {type: 'average', name: '平均值'}
                ],
                silent: true
            }
        },{
            data: Attendance3.uniform,
            name: '当前年份',
            type: 'line',
            smooth: true,
            itemStyle: {
                color: '#90ca8f',
            },
            markPoint: {
                symbol: 'rect',
                symbolSize: [50, 25],
                data: [{
                    x: '96%',
                    y: 65,
                    value: '校服校徽'
                }],
                silent: true
            },
            markLine: {
                data: [
                    {type: 'average', name: '平均值'}
                ],
                silent: true
            }
        },{
            data: Attendance4.late,
            name: '当前月份',
            type: 'line',
            smooth: true,
            itemStyle: {
                color: '#df6b66'
            },
            markPoint: {
                symbol: 'rect',
                symbolSize: [50, 25],
                data: [{
                    x: '96%',
                    y: 15,
                    value: '迟到晚到'
                }],
                silent: true
            },
            markLine: {
                data: [
                    {type: 'average', name: '平均值'}
                ],
                silent: true
            }
        },{
            data: Attendance4.early,
            name: '当前月份',
            type: 'line',
            smooth: true,
            itemStyle: {
                color:  '#71b9bc',
            },
            markPoint: {
                symbol: 'rect',
                symbolSize: [50, 25],
                data: [{
                    x: '96%',
                    y: 40,
                    value: '离校早退'
                }],
                silent: true
            },
            markLine: {
                data: [
                    {type: 'average', name: '平均值'}
                ],
                silent: true
            }
        },{
            data: Attendance4.uniform,
            name: '当前月份',
            type: 'line',
            smooth: true,
            itemStyle: {
                color: '#90ca8f',
            },
            markPoint: {
                symbol: 'rect',
                symbolSize: [50, 25],
                data: [{
                    x: '96%',
                    y: 65,
                    value: '校服校徽'
                }],
                silent: true
            },
            markLine: {
                data: [
                    {type: 'average', name: '平均值'}
                ],
                silent: true
            }
        }]
    };
        return (
            <Card>
                <Card.Header>
                    <h4>1-4-6 异常考勤比例</h4>
                </Card.Header>
                <Card.Body>
                    <Ec option={option} h='280px'/>
                </Card.Body>
            </Card>
        )
}