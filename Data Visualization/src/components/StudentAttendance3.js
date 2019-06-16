import React from 'react';
import { Card } from 'react-bootstrap';
import StudentAttendance4 from './StudentAttendance4';
import StudentAttendance5 from './StudentAttendance5';
import Ec from './Ec'

const xlabel = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
const dataset = {'student': [3, 0, 4, 3, 0, 0, 0, 0, 0, 2, 0, 0], 'class': [5, 1, 0, 6, 1, 4, 0, 0, 0, 8, 6, 9], 'school': [7, 0, 5, 4, 6, 5, 0, 0, 8, 6, 1, 7]}

export default function(){
    const option = {
        title: {
            text: '迟到晚到次数',
            textStyle: {
                fontSize: 12 
            }
        },
        legend: {
            data: ['学生', '班级平均', '学校平均']
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                axis: 'x',
                type: 'shadow',
            }
        },
        grid: {
            left: 0,
            right: 0,
            top: '15%',
            bottom: '8%',
            containLabel: true
        },
        xAxis: {
            type: 'category',
            data: xlabel,
            axisTick: {
                show: false
            },
        },
        yAxis: {
            type: 'value',
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
            name: '学生',
            itemStyle: {
                color: '#df6b66'
            },
            data: dataset.student,
            type: 'line'
        },{
            name: '班级平均',
            itemStyle: {
                color: '#90ca8f'
            },
            data: dataset.class,
            type: 'line'
        },{
             name: '学校平均',
            itemStyle: {
                color: '#7189aa'
            },
            data: dataset.school,
            type: 'line'
        }]
    };
    return (
        <Card>
            <Card.Header>
                <h4>3-5 异常考勤统计</h4>
            </Card.Header>
            <Card.Body>
                <Ec option={option} h='200px'/>
                <StudentAttendance4/>
                <StudentAttendance5/>
            </Card.Body>
        </Card>
    )
}    