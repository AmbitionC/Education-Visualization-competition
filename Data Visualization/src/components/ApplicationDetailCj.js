import React from 'react';
import { Table , Input , Button , Icon } from 'antd';
import Highlighter from 'react-highlight-words';
import jsonData from '../data/ori_data/cj.json';
 
export default class extends React.Component {
    state = {
        searchText: '',
    };
    getColumnSearchProps = (dataIndex) => ({
        filterDropdown: ({setSelectedKeys, selectedKeys, confirm, clearFilters}) => (
        <div style={{ padding: 8 }}>
            <Input
            ref={node => { this.searchInput = node; }}
            value={selectedKeys[0]}
            onChange={e => setSelectedKeys(e.target.value ? [e.target.value] : [])}
            onPressEnter={() => this.handleSearch(selectedKeys, confirm)}
            style={{ width: 188, marginBottom: 8, display: 'block' }}
            />
            <Button
            type="primary"
            onClick={() => this.handleSearch(selectedKeys, confirm)}
            icon="search"
            size="small"
            style={{ width: 90, marginRight: 8 }}
            >
            查找
            </Button>
            <Button
            onClick={() => this.handleReset(clearFilters)}
            size="small"
            style={{ width: 90 }}
            >
            重置
            </Button>
        </div>
        ),
        filterIcon: filtered => <Icon type="search" style={{ color: filtered ? '#1890ff' : undefined }} />,
        onFilter: (value, record) => record[dataIndex].toString().toLowerCase().includes(value.toLowerCase()),
        onFilterDropdownVisibleChange: (visible) => {
        if (visible) {
            setTimeout(() => this.searchInput.select());
        }
        },
        render: (text) => (
        <Highlighter
            highlightStyle={{ backgroundColor: '#ffc069', padding: 0 }}
            searchWords={[this.state.searchText]}
            autoEscape
            textToHighlight={text.toString()}
        />
        ),
    })

    handleSearch = (selectedKeys, confirm) => {
        confirm();
        this.setState({ searchText: selectedKeys[0] });
    }

    handleReset = (clearFilters) => {
        clearFilters();
        this.setState({ searchText: '' });
    }

    render() {
        const columns = [{
            title: '学生ID',
            dataIndex: 'stu_id',
            key: 'stu_id',
            width: '6%',
            ...this.getColumnSearchProps('stu_id'),
        }, {
            title: '考试ID',
            dataIndex: 'test_id',
            key: 'test_id',
            width: '6%',
            ...this.getColumnSearchProps('test_id'),
        }, {
            title: '考试编码',
            dataIndex: 'exam_number',
            key: 'exam_number',
            width: '6%',
            ...this.getColumnSearchProps('exam_number'),
        }, {
            title: '考试名称',
            dataIndex: 'exam_name',
            key: 'exam_name',
            width: '19%',
            ...this.getColumnSearchProps('exam_name'),
        }, {
            title: '考试学期',
            dataIndex: 'term',
            key: 'term',
            width: '11%',
            ...this.getColumnSearchProps('term'),
        }, {
            title: '考试类型',
            dataIndex: 'exam_type',
            key: 'exam_type',
            width: '6%',
            ...this.getColumnSearchProps('exam_type'),
        }, {
            title: '考试时间',
            dataIndex: 'exam_date',
            key: 'exam_date',
            width: '7%',
            ...this.getColumnSearchProps('exam_date'),
        }, {
            title: '科目ID',
            dataIndex: 'sub_id',
            key: 'sub_id',
            width: '6%',
            ...this.getColumnSearchProps('sub_id'),
        }, {
            title: '考试科目',
            dataIndex: 'sub_name',
            key: 'sub_name',
            width: '6%',
            ...this.getColumnSearchProps('sub_name'),
        }, {
            title: '考试成绩',
            dataIndex: 'mes_Score',
            key: 'mes_Score',
            width: '6%',
            ...this.getColumnSearchProps('mes_Score'),
        }, {
            title: 'Z成绩',
            dataIndex: 'mes_Z_Score',
            key: 'mes_Z_Score',
            width: '7%',
            ...this.getColumnSearchProps('mes_Z_Score'),
        }, {
            title: 'T成绩',
            dataIndex: 'mes_T_Score',
            key: 'mes_T_Score',
            width: '7%',
            ...this.getColumnSearchProps('mes_T_Score'),
        }, {
            title: '等第成绩',
            dataIndex: 'mes_dengdi',
            key: 'mes_dengdi',
            width: '7%',
            ...this.getColumnSearchProps('mes_dengdi'),
        }];
        return <Table columns={columns} dataSource={jsonData} />;
    }
}
