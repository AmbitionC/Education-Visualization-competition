import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';
import Attendance5 from '../data/schoolAttendance/Attendance_5.json' 

function data_preprocess(){
    const dataset = Attendance5.calenda;
    let len = dataset.length;
    for(var i = 0; i < len; i ++){
        let data_array = dataset[i];
        if(data_array[1] < 30){
            data_array[1] = data_array[1] * 20;
        }else if(data_array[1] < 100){
            data_array[1] = data_array[1] * 6;
        }else if(data_array[1] < 300){
            data_array[1] = data_array[1] * 1.8;
        }
        dataset[i] = data_array[1]

        
        dataset[i] = data_array
    }
    return dataset
}

export default function() {
    const option = {
        tooltip: {
            formatter: function (params) {
                return [
                    '日期：' + params.data[0],
                    '正常考勤人数：' + params.data[1] + '人'
                ].join('<br/>')
            }    
        },
        calendar: {
            top: '16%',
            left: '2%',
            cellSize: 'auto',
            range: ['2018-01-01', '2018-12-31'],
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
        series: [ {
            type: 'scatter',
            itemStyle: {
                color: 'rgb(113,155,129)'
            },
            coordinateSystem: 'calendar',
            
            symbolSize: function (val) {
                return val[1] / 40;
            },
            data: data_preprocess()
        }]
    }
    return (
        <Card>
            <Card.Header>
                <h4>1-4-4 学校正常到勤统计</h4>
            </Card.Header>
            <Card.Body>
                <Ec option={option} h='260px'/>
            </Card.Body>
        </Card>
    );
}

