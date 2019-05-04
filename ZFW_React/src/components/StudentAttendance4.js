import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec'

const xlabel = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'];
const dataset = {'student': [2, 0, 0, 3, 1, 2, 0, 0, 4, 0, 0, 3], 'class': [7, 4, 3, 5, 2, 4, 0, 0, 4, 2, 1, 1], 'school': [4, 4, 7, 8, 7, 0, 0, 0, 2, 7, 0, 4]}
export default function(){
    const option = {
        legend: {
            left: 'left',
            data: ['学生', '班级平均', '学校平均']
        },
        tooltip: {},
        toolbox: {
            show: true,
            feature: {
                dataView: {show: true, readOnly: false},
                magicType: {
                    type: ['bar', 'line']
                },
                restore: {show: true},
                saveAsImage: {show: true}
            }
        },
        xAxis: {
            name: '月份',
            type: 'category',
            data: xlabel
        },
        yAxis: {
            name: '次数',
            type: 'value'
        },
        series: [{
            name: '学生',
            itemStyle: {
                color: '#ff9797'
            },
            data: dataset.student,
            type: 'line'
        },{
            name: '班级平均',
            itemStyle: {
                color: '#a3d1d1'
            },
            data: dataset.class,
            type: 'line'
        },{
             name: '学校平均',
            itemStyle: {
                color: '#bebebe'
            },
            data: dataset.school,
            type: 'line'
        }]
    };
    return (
        <Card>
            <Card.Header>
                <h4>早退离校数据统计</h4>
            </Card.Header>
            <Card.Body>
                <Ec option={option} h='200px'/>
            </Card.Body>
        </Card>
    )
}    