import proyecto_web.contants as const

async def repo() -> str:
    return const.CODIGO_PAGINA_WEB_GITHUB

async def live(user:str) -> bool:
    if user == "armandoxxlml":
        return True
    else:
        return False
