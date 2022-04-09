import React from 'react'
import { auth, firestore } from '../firebase-config'
import { useCollectionData } from 'react-firebase-hooks/firestore'

function Home() {

  const dataRef = firestore.collection('garbage_history')
  const query = dataRef.orderBy('timestamp')
  
  const [garbageData] = useCollectionData(query, { idField: 'id' })

  return (
    <>
      <h2>History</h2>
      { garbageData && garbageData.map(info => <Garbage key={info.url} info={info} /> )}
    </>
  )
}

function Garbage(props) {
  
  const { uid, url, timestamp, category } = props.info
  
  if (auth.currentUser.uid !== uid) {
    return null
  }

  const date = timestamp.toDate().toLocaleString()
  return (
    <div className="garbage">
      <img width="300" src={url} alt="garbage" />
      <p><b>{category}</b> at {date}</p>
    </div>
  )

}

export default Home