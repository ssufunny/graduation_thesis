import React from 'react';
import styled from 'styled-components';
import TodoItem from './TodoItem';

const TodoListBlock = styled.div`
width: 300px;
height: 360px;
padding: 20px 32px;
padding-bottom: 48px;
overflow-y: auto;
margin: auto auto; /* 페이지 중앙에 나타나도록 설정 */
background: #e9ecef; /* 사이즈 조정이 잘 되고 있는지 확인하기 위한 임시 스타일 */
  `;

function TodoList() {
  return (
    <TodoListBlock>
      
    </TodoListBlock>
  );
}

export default TodoList;
