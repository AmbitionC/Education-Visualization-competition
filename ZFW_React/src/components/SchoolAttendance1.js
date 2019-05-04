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
        legend: [{
            data: ['学年统计', '学期统计', '当前年份', '当前月份'],
            selectedMode: 'single'
        }],
        xAxis: {
            name: '时间',
            type: 'category',
            max: 'dataMax',
            min: 'dataMin'
        },
        yAxis: {
            name: '百分比',
            type: 'value',
            max: 55,
            min: 'dataMin'
        },
        series: [{
            data: Attendance1.late,
            name: '学年统计',
            type: 'line',
            // smooth: true,
            itemStyle: {
                color: '#ff9797'
            },
            markPoint: {
                symbol: 'roundRect',
                data: [{
                    x: '4%',
                    y: '10%',
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
            // smooth: true,
            itemStyle: {
                color:  '#0080ff',
            },
            markPoint: {
                symbol: 'roundRect',
                data: [{
                    x: '4%',
                    y: '25%',
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
            // smooth: true,
            itemStyle: {
                color: '#6c6c6c',
            },
            markPoint: {
                symbol: 'roundRect',
                data: [{
                    x: '4%',
                    y: '40%',
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
            // smooth: true,
            itemStyle: {
                color: '#ff9797'
            },
            markPoint: {
                symbol: 'roundRect',
                data: [{
                    x: '4%',
                    y: '10%',
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
            // smooth: true,
            itemStyle: {
                color:  '#0080ff',
            },
            markPoint: {
                symbol: 'roundRect',
                data: [{
                    x: '4%',
                    y: '25%',
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
            // smooth: true,
            itemStyle: {
                color: '#6c6c6c',
            },
            markPoint: {
                symbol: 'roundRect',
                data: [{
                    x: '4%',
                    y: '40%',
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
            // smooth: true,
            itemStyle: {
                color: '#ff9797'
            },
            markPoint: {
                symbol: 'roundRect',
                data: [{
                    x: '4%',
                    y: '10%',
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
            // smooth: true,
            itemStyle: {
                color:  '#0080ff',
            },
            markPoint: {
                symbol: 'roundRect',
                data: [{
                    x: '4%',
                    y: '25%',
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
            // smooth: true,
            itemStyle: {
                color: '#6c6c6c',
            },
            markPoint: {
                symbol: 'roundRect',
                data: [{
                    x: '4%',
                    y: '40%',
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
            // smooth: true,
            itemStyle: {
                color: '#ff9797'
            },
            markPoint: {
                symbol: 'roundRect',
                data: [{
                    x: '4%',
                    y: '10%',
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
            // smooth: true,
            itemStyle: {
                color:  '#0080ff',
            },
            markPoint: {
                symbol: 'roundRect',
                data: [{
                    x: '4%',
                    y: '25%',
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
            // smooth: true,
            itemStyle: {
                color: '#6c6c6c',
            },
            markPoint: {
                symbol: 'roundRect',
                data: [{
                    x: '4%',
                    y: '40%',
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
                    <h4>考勤数据统计</h4>
                </Card.Header>
                <Card.Body>
                    <Ec option={option} h='400px'/>
                </Card.Body>
            </Card>
        )
}