export async function getStaticProps() {
    let error = null;
    let data = [1];
    let notfound = false;
    try{
        const res = await fetch('http://localhost:8000/api/showdiary');
        const data = await res.json();
    }catch(e){

        error = e;
    }

    if(!data.length){
        notfound = true;
    }
    return{
        props:{
            data : data,
            notfound : notfound
        }
    }

  }

  export default function about({data,error,notfound}){
    console.log(data);
    if(notfound){
        return(<>
        <h1>Not Found</h1>
        </>
        )
    }
  }