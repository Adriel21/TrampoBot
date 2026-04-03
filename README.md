# trampoBot

Agente inteligente de monitoramento de vagas de emprego. Cadastre seus interesses profissionais e receba automaticamente vagas relevantes de diversas fontes.

## O que faz

O trampoBot permite que um usuario informe criterios de busca (cargo, localizacao, senioridade, modelo de trabalho, palavras-chave) por uma **interface web** ou pelo **Telegram**, e retorna vagas estruturadas encontradas em diferentes plataformas.

## Fluxo de funcionamento

1. O usuario envia criterios de busca (web ou Telegram)
2. O sistema converte o texto em filtros estruturados
3. Um orquestrador dispara conectores de coleta para diferentes fontes
4. Os conectores executam automacao ou scraping controlado
5. O sistema normaliza os dados, remove duplicatas e classifica por relevancia
6. O usuario recebe uma lista de vagas com: titulo, empresa, localizacao, data da postagem, link, descricao, fonte e score de relevancia

## Arquitetura

O projeto segue uma arquitetura modular com separacao clara de responsabilidades:

```
frontend/telegram  ->  API backend  ->  interpretacao de filtros
                                              |
                                        orquestrador de buscas
                                              |
                                    conectores por fonte (Google, Greenhouse, Lever, ...)
                                              |
                                    pipeline de normalizacao -> deduplicacao -> ranking
                                              |
                                        persistencia (PostgreSQL)
                                              |
                                        notificacoes (Telegram / Web)
```

## Fontes de dados

- **Google Search** - busca geral de vagas
- **Paginas de carreira** de empresas
- **Plataformas de ATS** - Greenhouse, Lever e similares
- Outras plataformas via conectores especificos

Prioridade de coleta: APIs oficiais > extracao via HTML/rede > automacao com navegador (ultimo recurso).

## Stack

| Componente | Tecnologia |
|---|---|
| Backend | Python + FastAPI |
| Banco de dados | PostgreSQL |
| ORM | SQLAlchemy |
| Migracoes | Alembic |
| Fila/Jobs | Redis + Celery ou Dramatiq |
| Automacao web | Playwright |
| Telegram | Bot API |

## MVP

- API funcional com FastAPI
- Cadastro de preferencias do usuario
- Endpoint para iniciar busca
- Integracao basica com Telegram
- Pelo menos 2 conectores de vagas
- Persistencia em PostgreSQL
- Deduplicacao de resultados
- Retorno estruturado das vagas

## Requisitos

### Funcionais

- Cadastrar preferencias de vagas por usuario
- Buscar vagas manualmente e por agendamento
- Armazenar historico de vagas encontradas
- Evitar envio duplicado
- Integracao com Telegram
- Resultados organizados e legiveis
- Preparado para classificacao com IA e painel web futuros

### Nao funcionais

- Codigo modular e facil de manter
- Conectores independentes por fonte
- Logging de execucao
- Tratamento de falhas por fonte
- Arquitetura preparada para filas e jobs assincronos
- Facilidade para adicionar novas fontes
