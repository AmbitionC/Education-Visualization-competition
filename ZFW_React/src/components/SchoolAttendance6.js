import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';
import Attendance6 from '../data/schoolAttendance/Attendance_6.json' 
import Attendance7 from '../data/schoolAttendance/Attendance_7.json' 
import Attendance8 from '../data/schoolAttendance/Attendance_8.json' 
import Attendance9 from '../data/schoolAttendance/Attendance_9.json' 


function data_preprocess(dataset){
    // const dataset = Attendance6.calenda;
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
        legend : {
            show: true,
            data: ['异常考勤总量', '迟到晚到数量', '早退离校数量', '校服校徽数量'],
            selectedMode: 'single'
        },
        tooltip: {
            formatter: function (params) {
                return [
                    '日期：' + params.data[0],
                    '异常考勤人数：' + params.data[1] + '人'
                ].join('<br/>')
            }    
        },
        calendar: [
        {   
            yearLabel: {
                show: false,
            },
            left: 'center',
            monthLabel: {
                margin: 10
            },
            cellSize: 24,
            range: ['2018-01-01', '2018-12-31']
        }],
    
        series: [{
            type: 'scatter',
            name: '异常考勤总量',
            coordinateSystem: 'calendar',
            symbolSize: function (val) {
                return val[1] / 60;
            },
            data: data_preprocess(Attendance6.calenda)
        },{
            type: 'scatter',
            name: '迟到晚到数量',
            coordinateSystem: 'calendar',
            symbolSize: function (val) {
                return val[1] / 60;
            },
            data: data_preprocess(Attendance7.calenda)
        },{
            type: 'scatter',
            name: '早退离校数量',
            coordinateSystem: 'calendar',
            symbolSize: function (val) {
                return val[1] / 60;
            },
            data: data_preprocess(Attendance8.calenda)
        },{
            type: 'scatter',
            name: '校服校徽数量',
            coordinateSystem: 'calendar',
            symbolSize: function (val) {
                return val[1] / 60;
            },
            data: data_preprocess(Attendance9.calenda)
        }]
    }
    return (
        <Card>
            <Card.Header>
                <h4>学校异常考勤统计</h4>
            </Card.Header>
            <Card.Body>
                <Ec option={option} h='260px'/>
            </Card.Body>
        </Card>
    );
}

