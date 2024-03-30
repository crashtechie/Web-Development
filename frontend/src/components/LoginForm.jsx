import { useState } from 'react';
import api from '../api';
import { useNavigate } from 'react-router-dom';
import { ACCESS_TOKEN,REFRESH_TOKEN } from '../constants';
import '../styles/LoginForm.css';
import '../../node_modules/nes.css/css/nes.min.css'
//import LoadingIndicator from './LoadingIndicator';

function Form({route,method}) {
    const navigate = useNavigate();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [loading, setLoading] = useState(false);
    const name = method === 'login' ? 'Login' : 'Register';

    const handleSubmit = async (e) => {
        setLoading(true);
        e.preventDefault();
        
        try {
            const response = await api.post(route, { username, password });
            if (method === 'login') {
                localStorage.setItem(ACCESS_TOKEN, response.data.access);
                localStorage.setItem(REFRESH_TOKEN, response.data.refresh);
                navigate('/');
            } else {
                navigate('/login');
            }
        } catch (error) {
            alert(error);
        } finally {
            setLoading(false);
        }
    };

    return <form onSubmit={handleSubmit} className='login-container nes-container with-title'>
        <h1 class="title">{name}</h1>
        <input
            className='login-input nes-input'
            type='text'
            placeholder='Username'
            value={username}
            onChange={(e) => setUsername(e.target.value)}
        />
        <input
            className='login-input nes-input'
            type='password'
            placeholder='Password'
            value={password}
            onChange={(e) => setPassword(e.target.value)}
        />
        <button type='submit' className='nes-btn is-primary' disabled={loading}>
            {loading ? 'Loading...' : 'Login'}
        </button>
    </form>
}

export default Form;