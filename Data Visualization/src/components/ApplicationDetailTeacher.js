import React from 'react';
import { Table , Input , Button , Icon } from 'antd';
import Highlighter from 'react-highlight-words';
import jsonData from '../data/ori_data/tea.json';

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
            title: '教师ID',
            dataIndex: 'tea_id',
            key: 'tea_id',
            width: '8%',
            ...this.getColumnSearchProps('tea_id'),
        }, {
            title: '教师',
            dataIndex: 'tea_name',
            key: 'tea_name',
            width: '14%',
            ...this.getColumnSearchProps('tea_name'),
        }, {
            title: '学期',
            dataIndex: 'term',
            key: 'term',
            width: '22%',
            ...this.getColumnSearchProps('term'),
        }, {
            title: '年级',
            dataIndex: 'grade',
            key: 'grade',
            width: '14%',
            ...this.getColumnSearchProps('grade'),
        }, {
            title: '科目',
            dataIndex: 'sub_name',
            key: 'sub_name',
            width: '14%',
            ...this.getColumnSearchProps('sub_name'),
        }, {
            title: '科目ID',
            dataIndex: 'sub_id',
            key: 'sub_id',
            width: '7%',
            ...this.getColumnSearchProps('sub_id'),
        }, {
            title: '班级',
            dataIndex: 'cla_name',
            key: 'cla_name',
            width: '14%',
            ...this.getColumnSearchProps('cla_name'),
        }, {
            title: '班级ID',
            dataIndex: 'cla_id',
            key: 'cla_id',
            width: '7%',
            ...this.getColumnSearchProps('cla_id'),
        }];
        return <Table columns={columns} dataSource={jsonData} />;
    }
}
