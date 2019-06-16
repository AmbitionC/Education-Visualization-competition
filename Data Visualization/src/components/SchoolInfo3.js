import React from 'react';
import { Card } from 'react-bootstrap';
import Ec from './Ec';
import 'echarts/map/js/china';
import 'echarts/map/js/province/zhejiang';

export default function() {
    //来源
    const PROVINCE = [
        {name: '北京', value: 2},
        {name: '上海', value: 4},
        {name: '天津', value: 1},
        {name: '重庆', value: 5},
        {name: '河北', value: 7},
        {name: '山西', value: 5},
        {name: '辽宁', value: 7},
        {name: '吉林', value: 2},
        {name: '河南', value: 14},
        {name: '江苏', value: 35},
        {name: '浙江', value: 1336},
        {name: '安徽', value: 40},
        {name: '福建', value: 9},
        {name: '江西', value: 43},
        {name: '山东', value: 13},
        {name: '湖北', value: 23},
        {name: '湖南', value: 22},
        {name: '广东', value: 1},
        {name: '四川', value: 12},
        {name: '贵州', value: 3},
        {name: '陕西', value: 11},
        {name: '甘肃', value: 7},
        {name: '黑龙江', value: 7},
        {name: '广西', value: 1},
        {name: '台湾', value: 1},
    ];
    const CITY = [
        {name: '宁波市', value: 414},
        {name: '舟山市', value: 4},
        {name: '金华市', value: 6},
        {name: '杭州市', value: 9},
        {name: '台州市', value: 5},
        {name: '嘉兴市', value: 3},
        {name: '温州市', value: 5},
        {name: '衢州市', value: 2},
        {name: '绍兴市', value: 13},
        {name: '丽水市', value: 1},
    ];
    const getMapOption = function (map, min, max, data) {
        const layOutSize = map==='china'?'120%':'100%';
        return {
            tooltip: {
                formatter: (params) => {
                    if (params.data) {
                        return '来自'+ params.data.name + ': ' + params.data.value + '人';
                    } else {
                        return '0人';
                    }
                }
            },
            visualMap: {
                min: min,
                max: max,
                text:[max + '人', min],
                realtime: true,
                inRange: {
                    color: ['#8cc1aa', '#efdd7d', '#df6b66']
                }
            },
            series: [{
                type: 'map',
                map: map,
                layoutCenter: ['50%', '50%'],
                layoutSize: layOutSize,
                label: {
                    show: true,
                    position: [10,10],
                    fontSize: '8',
                    color: '#0b346e',
                },
                data: data
            }]
        };
    };
    return (
        <Card>
            <Card.Header>
                <h4>1-1-3 生源地分布</h4>
            </Card.Header>
            <Card.Body>
                <div className='row'>
                    <div className='col-12 col-lg-6'>
                        <Ec option={getMapOption('china', 0, 50, PROVINCE)} h='360px'/>
                    </div>
                    <div className='col-12 col-lg-6'>
                        <Ec option={getMapOption('浙江', 0, 20, CITY)} h='360px'/>
                    </div>
                </div>
            </Card.Body>
        </Card>
    );
}
