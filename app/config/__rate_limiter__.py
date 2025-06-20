from functools import wraps
from flask import request, flash, redirect, url_for
import time

# Dicionário para armazenar as tentativas por IP
rate_limit_data = {}

def rate_limiter(limit=3, window=60, message="Limite de requisições excedido. Tente novamente mais tarde.", page="bp_home.home"):

    def decorator(f):
        
        @wraps(f)
        def wrapper(*args, **kwargs):
            # Obtém o IP do cliente
            ip = request.remote_addr
            current_time = time.time()

            # Remove registros antigos
            if ip in rate_limit_data:
                rate_limit_data[ip] = [t for t in rate_limit_data[ip] if current_time - t <= window]
            else:
                rate_limit_data[ip] = []

            # Verifica se o limite foi excedido
            if len(rate_limit_data.get(ip, [])) >= limit:
                flash('danger',message)  # Envia uma mensagem para o flash
                return redirect(url_for(page))

            # Adiciona o timestamp da requisição
            rate_limit_data[ip].append(current_time)

            # Executa a função original
            return f(*args, **kwargs)
        return wrapper
    return decorator
