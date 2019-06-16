import React from 'react';
import { Card } from 'react-bootstrap';
import Intro from './Intro';
import Ec from './Ec';
import ywData from '../data/teacher/sankey_data/Teacher_class_0.json';
import ywLink from '../data/teacher/sankey_data/Teacher_link_0.json';
import ssData from '../data/teacher/sankey_data/Teacher_class_1.json';
import ssLink from '../data/teacher/sankey_data/Teacher_link_1.json';
import yyData from '../data/teacher/sankey_data/Teacher_class_2.json';
import yyLink from '../data/teacher/sankey_data/Teacher_link_2.json';
import wlData from '../data/teacher/sankey_data/Teacher_class_3.json';
import wlLink from '../data/teacher/sankey_data/Teacher_link_3.json';
import hxData from '../data/teacher/sankey_data/Teacher_class_4.json';
import hxLink from '../data/teacher/sankey_data/Teacher_link_4.json';
import zzData from '../data/teacher/sankey_data/Teacher_class_5.json';
import zzLink from '../data/teacher/sankey_data/Teacher_link_5.json';
import lsData from '../data/teacher/sankey_data/Teacher_class_6.json';
import lsLink from '../data/teacher/sankey_data/Teacher_link_6.json';
import swData from '../data/teacher/sankey_data/Teacher_class_7.json';
import swLink from '../data/teacher/sankey_data/Teacher_link_7.json';
import dlData from '../data/teacher/sankey_data/Teacher_class_8.json';
import dlLink from '../data/teacher/sankey_data/Teacher_link_8.json';
import jsData from '../data/teacher/sankey_data/Teacher_class_9.json';
import jsLink from '../data/teacher/sankey_data/Teacher_link_9.json';
import msData from '../data/teacher/sankey_data/Teacher_class_10.json';
import msLink from '../data/teacher/sankey_data/Teacher_link_10.json';
import tyData from '../data/teacher/sankey_data/Teacher_class_11.json';
import tyLink from '../data/teacher/sankey_data/Teacher_link_11.json';
import musicData from '../data/teacher/sankey_data/Teacher_class_12.json';
import musicLink from '../data/teacher/sankey_data/Teacher_link_12.json';

export default function() {
    const sub_cla = {
        '语文': [ywData, ywLink],
        '数学': [ssData, ssLink],
        '英语': [yyData, yyLink],
        '物理': [wlData, wlLink],
        '化学': [hxData, hxLink],
        '生物': [swData, swLink],
        '政治': [zzData, zzLink],
        '历史': [lsData, lsLink],
        '地理': [dlData, dlLink],
        '技术': [jsData, jsLink],
        '体育': [tyData, tyLink],
        '美术': [msData, msLink],
        '音乐': [musicData, musicLink],
    };
    const getSeries = (name, data) => {
        data[0].map(items => {
            const color = items.name.indexOf('老师')===-1?'#90ca8f':'#71b9bc';
            items.itemStyle = {
                color: color
            };
            return items;
        });
        return {
            name: name,
            type: 'sankey',
            left: 0,
            right: 0,
            top: 30,
            bottom: 36,
            orient: 'vertical',
            focusNodeAdjacency: false,
            itemStyle: {
                borderWidth: 0,
            },
            draggable: false,
            data: data[0],
            links: data[1],
            label: {
                position: 'top',
                formatter: params => {
                    const idx = params.name.indexOf('老师');
                    if (idx !== -1) {
                        return params.name.slice(0, idx-1) + '\n' + params.name.slice(idx-1);
                    }
                    return params.name.slice(0, 2) + '\n' + params.name.slice(3, 5) + '班';
                },
                fontSize: 10
            },
            lineStyle: {
                normal: {
                    color: '#95aac9',
                }
            },
        };
    }
    let series = [];
    for (let name in sub_cla) {
        series.push(getSeries(name, sub_cla[name]));
    }
    let option = {
        color : ['#72a375', '#71b9bc', '#efdd7d', '#e79d88', '#df6b66'],
        legend: {
            bottom: 'bottom',
            selectedMode: 'single',
        },
        series: series
    };
    const content = [
        '设计理念: 同一学科下教师的图块宽度表示该教师带班数量',
        '功能: 通过对比教师带班数量，帮助校领导层了解教师压力，平衡教师带班数量',
    ];
    return (
        <Card>
            <div className='card-header'>
                <h4>1-2-3 教师-班级关系</h4>
                <Intro content={content} />
            </div>
            <Card.Body>
                <Ec option={option} h='320px'/>
            </Card.Body>
        </Card>
    );
}