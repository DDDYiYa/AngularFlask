import { Injectable,OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { SERVERADDRESS } from '../settings';

@Injectable({
  providedIn: 'root'
})
export class CommonService implements OnInit {

  constructor(private http : HttpClient) { }

  ngOnInit() { }

  helloUrl : string = SERVERADDRESS+"/hello/hello";
  readhello()
  {
    return this.http.get<string>(this.helloUrl)
  }
}
