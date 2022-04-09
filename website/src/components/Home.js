import React, { useState } from 'react'
import { Chart } from 'react-google-charts'
import { auth, firestore } from '../firebase-config'
import { useCollectionData } from 'react-firebase-hooks/firestore'

function Home() {

  return (
    <>
      <GarbageStats />
      <GarbageHistory />
    </>
  )

}

function GarbageStats() {
  
  const data = firestore.collection('garbage_history').where('uid', '==', auth.currentUser.uid)
  
  const trashQuery = data.where('category', '==', 'trash')
  const [trashCount, setTrashCount] = useState(0)
  trashQuery.get().then(snap => setTrashCount(snap.size))
  
  const recycleQuery = data.where('category', '==', 'recycle')
  const [recycleCount, setRecycleCount] = useState(0)
  recycleQuery.get().then(snap => setRecycleCount(snap.size))

  const compostQuery = data.where('category', '==', 'compost')
  const [compostCount, setCompostCount] = useState(0)
  compostQuery.get().then(snap => setCompostCount(snap.size))

  return (
    <> { (trashCount || recycleCount || compostCount) && 
      <div className="stats">
        <h2>Stats</h2>
        <Chart
          chartType="PieChart"
          data={[
            ['Category', 'Amount'],
            ['Trash', trashCount],
            ['Recycle', recycleCount],
            ['Compost', compostCount],
          ]}
          options={{
            colors: ['#333333', '#00bbee', '#00ff22']
          }}
          width="100%"
          height="400px"
        />
      </div>
    } </>
  )

}

function GarbageHistory() {
  const dataRef = firestore.collection('garbage_history')
  const query = dataRef.orderBy('timestamp', 'desc')
  
  const [garbageData] = useCollectionData(query, { idField: 'id' })

  return (
    <div className="history">
      <h2>History</h2>
      { garbageData && garbageData.map(info => <Garbage key={info.url} info={info} /> )}
    </div>
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