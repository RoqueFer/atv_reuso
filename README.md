
## Parte I – Questões Objetivas

**1.** Qual das alternativas representa melhor uma _vantagem prática_ do reuso de software em projetos reais?

A) Maior esforço de manutenção de sistemas.  
B) Aumento do tempo de desenvolvimento inicial.  
**C) Redução de retrabalho e aproveitamento de código já testado.**  
D) Eliminação de toda a documentação de sistemas.  
E) Padronização e aceleração do desenvolvimento.  

----------

**2.** Um hospital comprou um sistema pronto de gestão de pacientes, mas precisou alterar a forma como os atendimentos eram registrados para se adaptar ao software. Esse caso ilustra:

A) Benefício do reuso de software.  
B) Uso de microserviços.  
**C) Problema de adaptação de requisitos a sistemas de aplicação.**
D) Desenvolvimento ágil.  
E) Integração de bibliotecas externas.  

----------

**3.** Qual das opções está mais associada ao modelo **incremental** de desenvolvimento de software?

**A) Entregas parciais de funcionalidades com feedback contínuo dos usuários.**
B) Execução linear e rígida de fases.  
C) Maior dificuldade de adaptação a mudanças.  
D) Eliminação total da dívida técnica.  
E) Exclusivo para projetos acadêmicos.  

----------

**4.** Uma característica marcante do modelo **cascata** é:

A) Flexibilidade total a mudanças de requisitos a qualquer momento.  
B) Desenvolvimento simultâneo de todas as etapas.  
C) Protótipos rápidos entregues de forma contínua.
**D) Estrutura sequencial com alto custo de mudanças tardias.** 
E) Uso obrigatório de microserviços.  

----------

**5.** A principal vantagem do modelo **espiral** em relação ao cascata é:

A) Custos sempre mais baixos em qualquer cenário.  
B) Integração automática com sistemas prontos.  
C) Eliminação da necessidade de testes.  
D) Simplicidade de implementação em qualquer contexto.  
**E) Inclusão de análise de riscos e prototipação em cada ciclo.**  

----------

**6.** Qual das alternativas representa uma **desvantagem** no uso de plataformas No Code / Low Code?

A) Maior velocidade na prototipagem de MVPs.  
**B) Dependência da plataforma, dificultando migrações (vendor lock-in).**  
C) Redução do tempo para entregar soluções.  
D) Possibilidade de integrar APIs externas.  
E) Padronização da interface e componentes.  

----------

**7.** Sistemas ERP normalmente possuem:

**A) Banco de dados centralizado para diferentes áreas da empresa.**  
B) Ausência de módulos configuráveis.  
C) Foco exclusivo em pequenas startups.  
D) Rejeição a processos de negócio padronizados.  
E) Exclusividade para uso acadêmico.  

----------

**8.** No contexto de integração de sistemas de aplicação, qual é uma recomendação prática?

A) Ignorar contratos de nível de serviço (SLA).  
B) Usar apenas planilhas para garantir interoperabilidade.  
**C) Testar protótipos de integração antes de adotar definitivamente.**  
D) Evitar documentar decisões de projeto.  
E) Impedir o uso de APIs externas.  

----------

**9.** Qual é um dos _problemas_ associados ao reuso de software?

**A) Síndrome do "não inventado aqui".**
B) Redução do tempo de entrega.  
C) Uso eficaz de especialistas.  
D) Conformidade com padrões.  
E) Maior cobertura de testes.  

----------

**10.** O que diferencia uma biblioteca de um framework?

A) Ambos funcionam da mesma forma, sem diferenças.  
**B) Biblioteca é chamada pelo desenvolvedor; framework define o fluxo e chama o código do desenvolvedor.**  
C) Frameworks nunca podem ser usados em aplicações web.  
D) Bibliotecas só funcionam em sistemas operacionais específicos.  
E) Frameworks dispensam totalmente o uso de banco de dados.  

----------

## Parte II – Questões Dissertativas



**11.** Compare os modelos **cascata, incremental e espiral**. Em quais situações cada um é mais adequado e por quê?
Modelo cascata - Modelo de produção de software tradicional criado a base de modelos de produção do ambiente fabril/industrial, o projeto tem um começo, meio  e fim bem estruturados, é caracterizado por ser rígido com mudanças de escopo, sendo recomendado para projetos com escopo claro, definido e onde não haverá mudanças durante sua execução.
Modelo incremental - Modelo de desenvolvimento com entregas adicionais a cada etapa, o produto é construído em camadas onde cada camada consequente incrementa a camada anterior. Recomendável o uso em projetos onde é necessária certa tolerância a mudança e abertura para inovações dentro do projeto.
Modelo espiral - Modelo de desenvolvimento com prototipação em cada etapa, altamente tolerável a mudanças de escopo e produto. Recomendado para soluções que atendam a problemas voláteis.


----------

**12.** Explique o que são **sistemas de aplicação (COTS)**. Cite um exemplo real do mercado e descreva como eles são configurados para diferentes clientes.
R: São Softwares comerciais comprados diretamente de outras empresas, um exemplo pode ser o Btrix, eles são configurados por meio de código ou lógica interna (low-code/no-code) para personalizar ao critério do cliente, um exemplo dentro do btrix é criar categorias de produtos, tipos de venda, clientes e outras informações necessárias de vendas



----------

**13.** Quais são os principais **benefícios e desafios** de usar plataformas **No Code / Low Code** em projetos de software? Dê exemplos de situações práticas em que cada ponto aparece.
Benefícios - Rápida criação de produto, com plataformas low-code/no-code torna-se rápido sair do zero em um projeto, especialmente bom para protótipos ou provas de conceitos. Pouca necessidade de proficiência técnica, possibilita que produtos possam ser elaborados por membros com menos conhecimento da equipe.
Malefícios: Estagnação devido código gerado por I.A, as alucinações da IA ficam mais prevalentes na medida que o trabalho cresce em complexidade, criando código pouco mantenível e se tornando um problema dentro do sistema. Vendor lock-in, ao utilizar ferramentas pagas é possível que seu software fique dependente de infraestruturas pagas o què pode aumentar custos e prejudicar eventuais avanços do projeto


----------

**14.** Uma empresa comprou um ERP, mas percebeu um grande descompasso entre o modelo do sistema e seus processos internos. Explique:

-   Por que isso pode acontecer. R: Erro na fase de pequisa sobre a solução o que pode gerar um descompasso entre o desejado e as capabilidades do ERP adquirido

-   Quais estratégias poderiam reduzir esse risco antes da adoção do sistema.
- Pesquisa mais bem conduzida, pedido de uma demo ou poc da solução para entender sua compatibilidade com os processos da empresa

----------

**15.** Uma universidade pretende substituir o Microsoft Office pelo LibreOffice. Explique por que essa decisão está relacionada ao **reuso de software** e quais seriam as vantagens e limitações dessa escolha.
Migrar de uma solução autoral para uma de código livre está relacionada a reuso na medida em quê ao optar-se pelo Libre a universidade ganha mais capacidade de organizar seus próprios dados, saindo do vendors lock in, possíveis desvantagens são: 1 - Dificuldade de migração do MS office para o Libre. 2 - Dificuldade de uso do usuário final. 3 - Dificuldade de integrações do Libre com outras soluções utilizadas pela universidade


----------

## Parte III – Questão Prática


#### **4. Qual framework escolheu, link da documentação e trecho de código.**

-   **Qual framework escolheu:** Django
- 
-   **Link do repo da atividade:** https://github.com/RoqueFer/atv_reuso
- 


    
    -   Documentação Oficial do Django: [https://docs.djangoproject.com/en/stable/](https://docs.djangoproject.com/en/stable/)
        

        
-   **Um pequeno trecho de código de exemplo:**
    
    Este trecho de código, localizado no arquivo `views.py`, define a lógica para responder a uma requisição web. Ele cria uma lista de clientes em formato de dicionário Python e a retorna como uma resposta no formato JSON, que é ideal para APIs REST.
    
 Arquivo: clientes/views.py
Responsável por definir a lógica de uma rota.

from django.http import JsonResponse

def lista_clientes(request):
    """
    Esta função (view) retorna uma lista fixa de clientes
    em formato JSON.
    """
    dados_clientes = [
        {"id": 1, "nome": "Maria Silva", "email": "maria.silva@example.com"},
        {"id": 2, "nome": "João Pereira", "email": "joao.p@example.com"},
    ]

    # A classe JsonResponse converte o dicionário Python para JSON
    # e configura o cabeçalho HTTP 'Content-Type' para 'application/json'.
    return JsonResponse({"clientes": dados_clientes})

#### **5. Complemento em segurança: Autenticação e Login**

-   **O framework oferece recursos nativos para login/autenticação ou depende de bibliotecas externas?** O Django oferece um sistema robusto e completo de autenticação e autorização de forma **nativa**. Ele vem com o módulo `django.contrib.auth`, que gerencia usuários, grupos, permissões, sessões e hashing de senhas de forma segura por padrão, seguindo as melhores práticas do mercado.
    
-   **Esse suporte facilita a vida do desenvolvedor ou exige muito esforço manual?** Ele **facilita enormemente** a vida do desenvolvedor. Ao invés de construir do zero um sistema complexo e suscetível a falhas de segurança (como armazenamento de senhas, controle de sessão, proteção contra ataques), o desenvolvedor já recebe uma solução pronta, testada pela comunidade e segura.
    
-   **Em sua visão, a segurança nesse framework é mais padronizada ou mais aberta?** A segurança é definitivamente mais **padronizada**. A filosofia do Django é "baterias inclusas" (batteries-included), oferecendo soluções prontas e reutilizáveis para os problemas mais comuns do desenvolvimento web. Isso garante um alto nível de segurança e consistência entre projetos, evitando que cada desenvolvedor "reinvente a roda" de forma insegura.
    

#### **6. Reflexão sobre reuso: Como o framework representa reuso de software.**

O Django é um exemplo clássico de reuso de software em múltiplas camadas. Em vez de escrever código do zero para se comunicar com o banco de dados, gerenciar URLs, tratar requisições HTTP ou autenticar usuários, nós **reusamos** os componentes que o framework oferece. A estrutura de "apps" reutilizáveis, o sistema de ORM (Mapeamento Objeto-Relacional) e o módulo de autenticação são abstrações poderosas que encapsulam funcionalidades complexas, permitindo que o desenvolvedor se concentre na lógica de negócio específica da aplicação, aumentando drasticamente a produtividade e a segurança.
