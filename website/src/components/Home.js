import React from 'react'

function Home() {

  // sample info
  const info = {
    url: "https://inbound.betterpackages.com/hubfs/AdobeStock_49089142.jpeg",
    timestamp: "2020-01-01 12:00:00",
    category: "RECYCLE"
  }

  return (
    <>
      <h2>History</h2>
      <Garbage info={info}></Garbage>
    </>
  )
}

function Garbage(props) {
  
  const { url, timestamp, category } = props.info;
  
  return (
    <div className="garbage">
      <img width="300" src={url} alt="garbage" />
      <p><b>{category}</b> at {timestamp}</p>
    </div>
  )

}

export default Home